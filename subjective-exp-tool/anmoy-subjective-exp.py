import sys
import os
import subprocess
import uuid
import csv
import random
from itertools import combinations
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                             QPushButton, QLabel, QFrame, QGridLayout,
                             QTextEdit)
from PyQt6.QtCore import QThread, pyqtSignal, Qt
from PyQt6.QtGui import QFont

# --- Configuration ---
MODELS_BASE_DIR = 'xxxxxxxx'
VOTES_FILE = 'pairwise_result.csv'
CODE_SUB_DIR = 'xxxxx'

# Worker for running a SINGLE pair of scripts (Unchanged)
class RunScriptsWorker(QThread):
    left_started = pyqtSignal(); left_finished = pyqtSignal(dict)
    right_started = pyqtSignal(); right_finished = pyqtSignal(dict)
    sequence_finished = pyqtSignal(); error_occurred = pyqtSignal(str)
    def __init__(self, script_a_path, script_b_path):
        super().__init__()
        self.script_a_path, self.script_b_path = script_a_path, script_b_path
    def run(self):
        try:
            self.left_started.emit()
            p_a = subprocess.Popen([sys.executable, self.script_a_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding='utf-8')
            out_a, err_a = p_a.communicate(timeout=300)
            self.left_finished.emit({'stdout': out_a, 'stderr': err_a, 'returncode': p_a.returncode})
            self.right_started.emit()
            p_b = subprocess.Popen([sys.executable, self.script_b_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding='utf-8')
            out_b, err_b = p_b.communicate(timeout=300)
            self.right_finished.emit({'stdout': out_b, 'stderr': err_b, 'returncode': p_b.returncode})
            self.sequence_finished.emit()
        except Exception as e:
            self.error_occurred.emit(f"A critical error occurred in worker thread: {str(e)}")

# Main Window Class
class VotingApp(QWidget):
    def __init__(self):
        super().__init__()
        self.worker = None
        self.evaluation_pool = []
        self.current_comparison_data = {}
        self.total_comparisons = 0
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Anonymous Pairwise Comparison Tool')
        self.setGeometry(100, 100, 1400, 950) 
        main_layout = QVBoxLayout(); self.setLayout(main_layout)
        
        config_layout = QHBoxLayout()
        self.start_button = QPushButton("Start New Session")
        config_layout.addWidget(self.start_button)
        main_layout.addLayout(config_layout)

       
        action_layout = QHBoxLayout()
        self.action_type_label = QLabel("Action Type: N/A")
        self.action_type_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.action_type_label.setStyleSheet("border: 1px solid #c0c0c0; padding: 6px; margin-top: 5px; font-weight: bold;")
        action_layout.addWidget(self.action_type_label)
        main_layout.addLayout(action_layout)
        
        # Display Area
        display_layout = QGridLayout()
        self.label_model_a = QLabel("Model A"); self.label_model_a.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.display_left = QTextEdit(); self.display_left.setReadOnly(True); self.display_left.setFont(QFont("Courier New", 10))
        self.label_model_b = QLabel("Model B"); self.label_model_b.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.display_right = QTextEdit(); self.display_right.setReadOnly(True); self.display_right.setFont(QFont("Courier New", 10))
        display_layout.addWidget(self.label_model_a, 0, 0); display_layout.addWidget(self.label_model_b, 0, 1)
        display_layout.addWidget(self.display_left, 1, 0); display_layout.addWidget(self.display_right, 1, 1)
        main_layout.addLayout(display_layout)
        
        # Voting Panel
        vote_layout = QHBoxLayout()
        self.vote_left_button, self.vote_right_button, self.vote_tie_button, self.vote_both_bad_button = QPushButton("Left is Better"), QPushButton("Right is Better"), QPushButton("It's a Tie"), QPushButton("Both are Bad")
        vote_layout.addStretch(1); vote_layout.addWidget(self.vote_left_button); vote_layout.addWidget(self.vote_right_button); vote_layout.addWidget(self.vote_tie_button); vote_layout.addWidget(self.vote_both_bad_button); vote_layout.addStretch(1)
        main_layout.addLayout(vote_layout)
        
        # Navigation Panel
        nav_layout = QHBoxLayout()
        self.status_label, self.run_pair_button, self.next_button = QLabel("Welcome!"), QPushButton("Run Current Pair"), QPushButton("Next")
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        nav_layout.addWidget(self.status_label, 1); nav_layout.addWidget(self.run_pair_button); nav_layout.addWidget(self.next_button)
        main_layout.addLayout(nav_layout)
        
        self.start_button.clicked.connect(self.start_new_session)
        self.next_button.clicked.connect(self.select_next_pair)
        self.run_pair_button.clicked.connect(self.execute_current_pair)
        self.vote_left_button.clicked.connect(lambda: self.record_vote("left")); self.vote_right_button.clicked.connect(lambda: self.record_vote("right")); self.vote_tie_button.clicked.connect(lambda: self.record_vote("tie")); self.vote_both_bad_button.clicked.connect(lambda: self.record_vote("both_bad"))
        
        self.set_initial_state();

    def set_initial_state(self):
        self.set_voting_buttons_enabled(False); self.run_pair_button.setEnabled(False); self.next_button.setEnabled(False); self.start_button.setEnabled(True)
        self.display_left.clear(); self.display_right.clear()
        self.status_label.setText("Welcome! Click 'Start New Session' to begin.")
        self.action_type_label.setText("Action Type: N/A")

    def set_voting_buttons_enabled(self, enabled):
        self.vote_left_button.setEnabled(enabled); self.vote_right_button.setEnabled(enabled); self.vote_tie_button.setEnabled(enabled); self.vote_both_bad_button.setEnabled(enabled)

    def get_task_identifier(self, filename):
        """Gets content AFTER the first underscore (used for pairing)."""
        if '_' in filename: return filename.split('_', 1)[1].lower().strip()
        return filename.lower().strip()
        
    def get_action_type(self, filename):
        """NEW: Gets content between the first underscore and .py extension."""
        if '_' in filename and filename.endswith('.py'):
            task_part = filename.split('_', 1)[1]
            action_type = task_part.rsplit('.py', 1)[0]
            return action_type
        return "Unknown"

    def start_new_session(self):
        self.status_label.setText("Building comparison pool..."); QApplication.processEvents()
        self.evaluation_pool = []
        try:
            if not os.path.exists(MODELS_BASE_DIR): raise FileNotFoundError(f"Base directory '{MODELS_BASE_DIR}' not found!")
            all_models = [d for d in os.listdir(MODELS_BASE_DIR) if os.path.isdir(os.path.join(MODELS_BASE_DIR, d, CODE_SUB_DIR))]
            if len(all_models) < 2: self.status_label.setText("Error: Need at least two valid models."); return
            model_pairs = combinations(all_models, 2)
            for model1, model2 in model_pairs:
                path1 = os.path.join(MODELS_BASE_DIR, model1, CODE_SUB_DIR); path2 = os.path.join(MODELS_BASE_DIR, model2, CODE_SUB_DIR)
                scripts_map1 = {self.get_task_identifier(f): f for f in os.listdir(path1) if f.endswith('.py')}
                scripts_map2 = {self.get_task_identifier(f): f for f in os.listdir(path2) if f.endswith('.py')}
                common_tasks = set(scripts_map1.keys()) & set(scripts_map2.keys())
                for task in common_tasks:
                    self.evaluation_pool.append(((model1, model2), (scripts_map1[task], scripts_map2[task])))
        except Exception as e: self.status_label.setText(f"Error during setup: {e}"); return
        if not self.evaluation_pool: self.status_label.setText("No common script tasks found."); self.set_initial_state(); return
        
        random.shuffle(self.evaluation_pool)
        self.total_comparisons = len(self.evaluation_pool)
        self.status_label.setText(f"Session started! {self.total_comparisons} unique comparisons loaded. Click 'Next'.")
        self.next_button.setEnabled(True); self.run_pair_button.setEnabled(False); self.start_button.setEnabled(False)

    def select_next_pair(self):
        """MODIFIED: Updates the action type label."""
        if not self.evaluation_pool:
            self.status_label.setText(f"All {self.total_comparisons} comparisons complete! Thank you."); self.set_initial_state(); return
        
        (model1, model2), (script1, script2) = self.evaluation_pool.pop()
        
        if random.random() < 0.5:
            self.current_comparison_data = {'left_model': model1, 'left_script': script1, 'right_model': model2, 'right_script': script2}
        else:
            self.current_comparison_data = {'left_model': model2, 'left_script': script2, 'right_model': model1, 'right_script': script1}
        
       
        action_type = self.get_action_type(self.current_comparison_data['left_script'])
        self.action_type_label.setText(f"Action Type: {action_type}")
        
        remaining = len(self.evaluation_pool)
        self.status_label.setText(f"Ready for next pair ({remaining} remaining). Click 'Run Current Pair'.")
        self.display_left.setText("(Pending run...)"); self.display_right.setText("(Pending run...)")
        self.display_left.setStyleSheet("color: gray;"); self.display_right.setStyleSheet("color: gray;")
        self.run_pair_button.setEnabled(True); self.next_button.setEnabled(False); self.set_voting_buttons_enabled(False)
        
    def execute_current_pair(self):
        if not self.current_comparison_data: return
        self.run_pair_button.setEnabled(False)
        left_script_path = os.path.join(MODELS_BASE_DIR, self.current_comparison_data['left_model'], CODE_SUB_DIR, self.current_comparison_data['left_script'])
        right_script_path = os.path.join(MODELS_BASE_DIR, self.current_comparison_data['right_model'], CODE_SUB_DIR, self.current_comparison_data['right_script'])
        self.worker = RunScriptsWorker(left_script_path, right_script_path)
        self.worker.left_started.connect(self.on_left_started); self.worker.left_finished.connect(self.on_left_finished)
        self.worker.right_started.connect(self.on_right_started); self.worker.right_finished.connect(self.on_right_finished)
        self.worker.sequence_finished.connect(self.on_sequence_finished); self.worker.error_occurred.connect(self.on_worker_error)
        self.worker.start()

    def on_left_started(self):
        self.status_label.setText(f"Running Model A..."); self.display_left.setStyleSheet("color: #d3d3d3;"); self.display_left.setText("Running script...")
    def on_left_finished(self, result):
        self._display_script_output(self.display_left, result)
    def on_right_started(self):
        self.status_label.setText(f"Running Model B..."); self.display_right.setStyleSheet("color: #d3d3d3;"); self.display_right.setText("Running script...")
    def on_right_finished(self, result):
        self._display_script_output(self.display_right, result)
    def on_sequence_finished(self):
        remaining = len(self.evaluation_pool)
        self.status_label.setText(f"Run complete. Please vote. ({remaining} remaining)")
        self.set_voting_buttons_enabled(True); self.next_button.setEnabled(True)
    def on_worker_error(self, error_message):
        self.status_label.setText("A critical error stopped the process."); self.display_left.setStyleSheet("color: red;"); self.display_left.setText(error_message)
        self.next_button.setEnabled(True)
    
    def _display_script_output(self, text_edit_widget, result):
        if result['returncode'] == 0:
            text_edit_widget.setStyleSheet("color: black;"); text_edit_widget.setText(result['stdout'] or "(No standard output)")
        else:
            text_edit_widget.setStyleSheet("color: red;"); text_edit_widget.setText(result['stderr'] or "(No standard error output)")

    def record_vote(self, winner):
        if not self.current_comparison_data: return
        data_to_log = {
            "model_left": self.current_comparison_data['left_model'], "model_right": self.current_comparison_data['right_model'],
            "script_left": self.current_comparison_data['left_script'], "script_right": self.current_comparison_data['right_script'],
            "winner": winner
        }
        self.status_label.setText(f"Vote recorded: {winner}. Please click 'Next'.")
        self.set_voting_buttons_enabled(False)
        file_exists = os.path.isfile(VOTES_FILE)
        with open(VOTES_FILE, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = data_to_log.keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if not file_exists: writer.writeheader()
            writer.writerow(data_to_log)
        self.current_comparison_data = {}

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet("QWidget { font-size: 15pt; }")
    ex = VotingApp()
    ex.show()
    sys.exit(app.exec())