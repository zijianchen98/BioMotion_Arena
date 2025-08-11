import os
os.environ['CUDA_VISIBLE_DEVICES'] = '0,1'

access_token = 'xxxxxx'
import subprocess
import re
from tqdm import tqdm
from transformers import AutoModelForCausalLM, AutoTokenizer


model_name = "Qwen/Qwen2.5-72B-Instruct"

name_tail = "qwen25-72b"

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype="auto",
    device_map="auto"
)

tokenizer = AutoTokenizer.from_pretrained(model_name)

# fine-grained

action_list = ['walking', 'running', 'waving a hand', 'jumping up', 'jumping forward', 'bowing', 'lying down', 'sitting down', 'turning around', 'forward rolling']

gender_list = ['man','woman']

happiness_list = ['happy','sad']

weight_list = ['heavy', 'light']

for action in tqdm(action_list): 
    for gender in gender_list:
        for happiness in happiness_list:
            for weight in weight_list:

                Question = "Question: write a Python program that shows a point-light stimulus animation which represents biological motion. \n Detailed Requirements: \n "

                prompt_action = "1. Subject and Action: The animation depict a "+ happiness + gender + " with " + weight +" weight is <" + action + ">. \n"

                prompt_style_quality = "2. Visual Style: The stimulus should consist of exactly 15 white point-lights moving against a solid black background. \n 3. Motion Quality: The animation must be realistic, coherent, and biomechanically plausible to accurately represent the specified human action. The movement should be smooth and natural. \n"

                prompt = Question +prompt_action +prompt_style_quality


                messages = [
                    {"role": "system", "content": "You are an expert Python programmer. You will be given a question (problem specification) and will generate a correct Python program that matches the specification and passes all tests. You will NOT return anything except for the program."},
                    {"role": "user", "content": prompt}
                ]



                text = tokenizer.apply_chat_template(
                    messages,
                    tokenize=False,
                    add_generation_prompt=True
                )
                model_inputs = tokenizer([text], return_tensors="pt").to(model.device)

                generated_ids = model.generate(
                    **model_inputs,
                    max_new_tokens=32768
                )
                generated_ids = [
                    output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
                ]

                response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]

                match = re.search(r'```python(.*?)```', response, re.DOTALL)
                if match:
                    code = match.group(1)

                file_path = "./"+name_tail+"/py_code_fine/"+name_tail+"_"+gender+"_"+weight+"_"+happiness+"_"+action+".py"

                try:
                    with open(file_path, 'w') as f:
                        f.write(code)
                    print(f"✅ Successfully created and saved to '{file_path}'")
                except Exception as e:
                    print(f"❌ An error occurred: {e}")




# basic version
for action in tqdm(action_list): 
    Question = "Question: write a Python program that shows a point-light stimulus animation which represents biological motion. \n Detailed Requirements: \n "

    prompt_action = "1. Subject and Action: The animation depict a man is " + action + ">. \n"

    prompt_style_quality = "2. Visual Style: The stimulus should consist of exactly 15 white point-lights moving against a solid black background. \n 3. Motion Quality: The animation must be realistic, coherent, and biomechanically plausible to accurately represent the specified human action. The movement should be smooth and natural. \n"

    prompt = Question + prompt_action +prompt_style_quality
    messages = [
        {"role": "system", "content": "You are an expert Python programmer. You will be given a question ( problem specification) and will generate a correct Python program that matches the specification and passes all tests. You will NOT return anything except for the program."},
        {"role": "user", "content": prompt}
    ]
    

    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )
    model_inputs = tokenizer([text], return_tensors="pt").to(model.device)

    generated_ids = model.generate(
        **model_inputs,
        max_new_tokens=32768
    )
    generated_ids = [
        output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
    ]

    response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]

    match = re.search(r'```python(.*?)```', response, re.DOTALL)
    if match:
        code = match.group(1)

    file_path = "./"+name_tail+"/py_code/"+name_tail+"_"+action+".py"

    try:
        with open(file_path, 'w') as f:
            f.write(code)
        print(f"✅ Successfully created and saved to '{file_path}'")
    except Exception as e:
        print(f"❌ An error occurred: {e}")
