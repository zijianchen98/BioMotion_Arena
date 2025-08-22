import gradio as gr
import base64
import re
import os
from openai import OpenAI
import random
import traceback
import subprocess
import csv
from datetime import datetime
import uuid
import argparse



# --- Core Functions ---

def encode_image(image_path):
    if not image_path: return None
    try:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
    except Exception as e:
        print(f"Error encoding image: {e}")
        return None

def extract_python_code(content):
    match = re.search(r'```python(.*?)```', content, re.DOTALL)
    if match: return match.group(1).strip()
    return content.strip()

def call_model_api(client, model_name, prompt, base64_image):
    try:
        messages = [
            {"role": "system", "content": "You are an expert Python programmer. You will be given a question (problem specification) and will generate a correct Python program that matches the specification. \
                You will NOT return anything except for the program."},
        ]
        user_content = [{"type": "text", "text": prompt}]
        if base64_image:
            user_content.append({"type": "image_url", "image_url": {"url": f"data:image/png;base64,{base64_image}"}})
        messages.append({"role": "user", "content": user_content})

        response = client.chat.completions.create(
            model=model_name,
            messages=messages,
            max_tokens=32768,
        )
        content = response.choices[0].message.content
        return extract_python_code(content)
    except Exception as e:
        error_message = f"--- ERROR ---\nModel: {model_name}\n{traceback.format_exc()}"
        print(error_message)
        return error_message

def run_generated_code(code):

    if not code:
        return "No code to run."
    
    script_filename = f"temp_script_{uuid.uuid4()}.py"
    try:
        with open(script_filename, "w", encoding="utf-8") as f:
            f.write(code)
        
        # Execute the script and capture its output
        result = subprocess.run(
            ["python", script_filename], 
            capture_output=True, 
            text=True, 
            timeout=60  
        )
        
        # Format the log output
        output_log = f"--- STDOUT ---\n{result.stdout.strip()}\n\n--- STDERR ---\n{result.stderr.strip()}"

        if result.returncode == 0:
            return f"✅ Script executed successfully.\n\n{output_log}"
        else:
            return f"❌ Script exited with error code {result.returncode}.\n\n{output_log}"

    except subprocess.TimeoutExpired:
        return "❌ Script execution timed out after 60 seconds."
    except Exception as e:
        return f"❌ An unexpected error occurred: {e}"
    finally:
        # Clean up the temporary script file
        if os.path.exists(script_filename):
            os.remove(script_filename)

def get_next_battle_id():
    if not os.path.exists(PREFERENCES_FILE): return 1
    try:
        with open(PREFERENCES_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
            if len(lines) < 2: return 1
            last_id = int(lines[-1].split(',')[0])
            return last_id + 1
    except:
        return 1

def save_preference(model_a_name, model_b_name, choice):
    header = ["battle_id", "model_a", "model_b", "preference"]
    battle_id = get_next_battle_id()
    if not os.path.exists(PREFERENCES_FILE):
        with open(PREFERENCES_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(header)
    with open(PREFERENCES_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([battle_id, model_a_name, model_b_name, choice])
    
    gr.Info(f"Feedback '{choice}' saved for Battle #{battle_id}!")
    return gr.update(value=f"### Model A ({model_a_name})"), gr.update(value=f"### Model B ({model_b_name})")

def generate_bio_motion_code(user_prompt, image_path):
    if not user_prompt or user_prompt.strip() == "":
        error_update = gr.update(value="Error: User Prompt cannot be empty.", lines=5)
        return error_update, error_update, None, None, gr.update(visible=False), None, None, "### Model A", "### Model B"
    
    if len(TOTAL_MODEL_POOL) < 2:
        error_update = gr.update(value="Error: Total models available must be at least 2.", lines=5)
        return error_update, error_update, None, None, gr.update(visible=False), None, None, "### Model A", "### Model B"

    model_a_name, model_b_name = random.sample(TOTAL_MODEL_POOL, 2)
    base64_image = encode_image(image_path)
    
    client_for_a = client if model_a_name in MODEL_LIST else client_special
    client_for_b = client if model_b_name in MODEL_LIST else client_special
    
    output_a = call_model_api(client_for_a, model_a_name, user_prompt, base64_image)
    output_b = call_model_api(client_for_b, model_b_name, user_prompt, base64_image)

    lines_a = len(output_a.splitlines())
    lines_b = len(output_b.splitlines())
    
    return (
        gr.update(value=output_a, lines=min(lines_a, MAX_CODE_LINES)),
        gr.update(value=output_b, lines=min(lines_b, MAX_CODE_LINES)),
        None, None,
        gr.update(visible=True),
        model_a_name, model_b_name,
        "### Model A", "### Model B"
    )

def update_reference_prompt(mode, action, gender, happiness, weight):
    if mode == "Basic":
        action_description = f"a man is <{action}>"
    else:
        action_description = f"a {happiness} {gender} with {weight} weight is <{action}>"
    question = "Question: Given an example image <image>, write a Python program that shows a point-light stimulus animation which represents biological motion.\nDetailed Requirements:\n"
    prompt_action = f"1. Subject and Action: The animation depicts {action_description}.\n"
    prompt_style_quality = "2. Visual Style: The stimulus should consist of exactly 15 white point-lights moving against a solid black background.\n3. Motion Quality: The animation must be realistic, coherent, and biomechanically plausible to accurately represent the specified human action. The movement should be smooth and natural. The style should be the same as the example image.\n"
    reference_prompt = question + prompt_action + prompt_style_quality
    return gr.update(value=reference_prompt), gr.update(value=reference_prompt)

def update_ui_for_mode(mode):
    is_fine_grained = (mode == "Fine-grained")
    return {
        gender_dd: gr.update(visible=is_fine_grained),
        happiness_dd: gr.update(visible=is_fine_grained),
        weight_dd: gr.update(visible=is_fine_grained),
    }

# --- Gradio UI Layout ---
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    model_a_state = gr.State()
    model_b_state = gr.State()

    gr.Markdown("# BioMotion Arena")
    gr.Markdown("Use the controls to generate a reference prompt, then edit or rewrite it in the final prompt box. Click 'Generate' to get code from two anonymous models, then run, compare, and vote.")

    with gr.Row():
        with gr.Column(scale=2):
            gr.Markdown("### 1. Input Controls")
            image_input = gr.Image(value='./ref.png', type='filepath', label="Upload Example Image (Optional)")
            mode_radio = gr.Radio(["Basic", "Fine-grained"], label="Generation Mode", value="Basic")
            action_list = ['walking', 'running', 'waving a hand', 'jumping up', 'jumping forward', 'bowing', 'lying down', 'sitting down', 'turning around', 'forward rolling']
            action_dd = gr.Dropdown(action_list, label="Action", value="walking")
            gender_dd = gr.Dropdown(['man', 'woman'], label="Gender", value="man", visible=False)
            happiness_dd = gr.Dropdown(['happy', 'sad', 'neutral'], label="Emotion", value="happy", visible=False)
            weight_dd = gr.Dropdown(['heavy', 'light', 'normal'], label="Weight", value="normal", visible=False)
            reference_prompt_output = gr.Textbox(label="💡 Reference Prompt (Auto-Generated)", lines=8, interactive=False)
            user_prompt_input = gr.Textbox(label="✍️ Your Final Prompt (Editable)", lines=8, interactive=True)
            generate_btn = gr.Button("🚀 Generate Code", variant="primary")

        with gr.Column(scale=5):
            gr.Markdown("### 2. Model Outputs & Comparison")
            with gr.Row():
                with gr.Column():
                    model_a_md = gr.Markdown("### Model A")
                    code_output_a = gr.Code(label="Generated by Model A", language="python")
                    run_button_a = gr.Button("Run Code A")
                    run_output_a = gr.Textbox(label="Run Output / Status", interactive=False, lines=8)
                with gr.Column():
                    model_b_md = gr.Markdown("### Model B")
                    code_output_b = gr.Code(label="Generated by Model B", language="python")
                    run_button_b = gr.Button("Run Code B")
                    run_output_b = gr.Textbox(label="Run Output / Status", interactive=False, lines=8)
            
            with gr.Group(visible=False) as preference_box:
                gr.Markdown("### 3. Which of the generated motion is better?")
                with gr.Row():
                    left_better_btn = gr.Button("Left is Better")
                    right_better_btn = gr.Button("Right is Better")
                    tie_btn = gr.Button("It's a Tie")
                    bad_btn = gr.Button("Both are Bad")
    
    # --- Event Listeners ---
    prompt_controls = [mode_radio, action_dd, gender_dd, happiness_dd, weight_dd]
    mode_radio.change(fn=update_ui_for_mode, inputs=mode_radio, outputs=[gender_dd, happiness_dd, weight_dd])
    for control in prompt_controls:
        control.change(fn=update_reference_prompt, inputs=prompt_controls, outputs=[reference_prompt_output, user_prompt_input])

    generate_outputs = [
        code_output_a, code_output_b, run_output_a, run_output_b,
        preference_box, model_a_state, model_b_state, model_a_md, model_b_md
    ]
    generate_btn.click(fn=generate_bio_motion_code, inputs=[user_prompt_input, image_input], outputs=generate_outputs)
    
    run_button_a.click(fn=run_generated_code, inputs=code_output_a, outputs=run_output_a)
    run_button_b.click(fn=run_generated_code, inputs=code_output_b, outputs=run_output_b)
    
    preference_outputs = [model_a_md, model_b_md]
    left_better_btn.click(fn=save_preference, inputs=[model_a_state, model_b_state, gr.State("Left is Better")], outputs=preference_outputs)
    right_better_btn.click(fn=save_preference, inputs=[model_a_state, model_b_state, gr.State("Right is Better")], outputs=preference_outputs)
    tie_btn.click(fn=save_preference, inputs=[model_a_state, model_b_state, gr.State("It's a Tie")], outputs=preference_outputs)
    bad_btn.click(fn=save_preference, inputs=[model_a_state, model_b_state, gr.State("Both are Bad")], outputs=preference_outputs)

    demo.load(fn=update_reference_prompt, inputs=prompt_controls, outputs=[reference_prompt_output, user_prompt_input])

if __name__ == "__main__":


    parser = argparse.ArgumentParser(description="Run the Gradio app with API keys provided as arguments.")
    parser.add_argument('--default-key', type=str, required=True, help='API key for the default API endpoint.')
    parser.add_argument('--special-key', type=str, required=True, help='API key for the special API endpoint.')
    args = parser.parse_args()


    global client_default, client_special
    
    
    DEFAULT_API_BASE_URL = "xxxxxx"

    DEFAULT_API_KEY = "xxxxxx"
    SPECIAL_API_KEY = "xxxxxx" 

    client = OpenAI(
        base_url=DEFAULT_API_BASE_URL,
        api_key=DEFAULT_API_KEY
    )

    MODEL_LIST = [
        "o4-mini-2025-04-16",
        "gpt-4o",
        "gpt-4-turbo",
        "o4-mini",
        "gpt-4.1-2025-04-14",
        "gpt-4.1-mini-2025-04-14",
        "gpt-4o-2024-05-13",
        "gpt-5-2025-08-07",
        "o3",
        "o3-mini",
        "o3-mini-2025-01-31",
        "grok-4",
        "grok-3",
        "grok-3-reasoning",
        "claude-opus-4-20250514",
        "claude-3-7-sonnet-20250219",
        "claude-sonnet-4-20250514-thinking",
        "claude-3-5-sonnet-20241022",
        "doubao-seed-1-6-flash-250615",
        "doubao-seed-1-6-250615",
        "deepseek-r1-2025-01-20",
        "deepseek-r1-250528",
        "deepseek-v3",
        "qwen3-235b-a22b",
        "qwen3-coder-plus",
        "qwen3-32b",
        "qwen-max-latest"
    ]



    # API 2: 
    # =================================================================
    SPECIAL_API_BASE_URL = DEFAULT_API_BASE_URL 
    SPECIAL_API_KEY = SPECIAL_API_KEY     

    MODEL_LIST2 = [
        "gemini-2.5-flash",                         
        "gemini-2.5-pro",
        "gemini-2.0-flash",
        "gemini-1.5-pro-latest",
        "gemini-1.5-flash-latest",
    ]
    # =================================================================

    client_special = OpenAI(
        base_url=SPECIAL_API_BASE_URL,
        api_key=SPECIAL_API_KEY
    )

    client_default = OpenAI(
    base_url=DEFAULT_API_BASE_URL,
    api_key=args.default_key
    )
    
    client_special = OpenAI(
        base_url=SPECIAL_API_BASE_URL,
        api_key=args.special_key
    )

    TOTAL_MODEL_POOL = MODEL_LIST + MODEL_LIST2
    PREFERENCES_FILE = "preferences.csv"
    MAX_CODE_LINES = 50

    print("API clients initialized successfully.")
    
    demo.launch()