import base64
import requests
from tqdm import tqdm
import time
import csv
import re
import os
from PIL import Image
from openai import OpenAI
import numpy as np
import subprocess
import re


# enter your own
client = OpenAI(
    base_url="xxxxxxxxxxxx",
    api_key="xxxxxxxxxx"
)


model_name = "o1"
name_tail = "o1"




action_list = ['walking','running', 'waving a hand', 'jumping up', 'jumping forward', 'bowing', 'lying down', 'sitting down', 'turning around', 'forward rolling']

gender_list = ['man','woman']

happiness_list = ['happy','sad']

weight_list = ['heavy', 'light']


# basic
for action in tqdm(action_list): 
    Question = "Question: write a Python program that shows a point-light stimulus animation which represents biological motion. \n Detailed Requirements: \n "

    prompt_action = "1. Subject and Action: The animation depict a man is <" + action + ">. \n"

    prompt_style_quality = "2. Visual Style: The stimulus should consist of exactly 15 white point-lights moving against a solid black background. \n 3. Motion Quality: The animation must be realistic, coherent, and biomechanically plausible to accurately represent the specified human action. The movement should be smooth and natural. \n"

    prompt = Question + prompt_action +prompt_style_quality
    
    response = client.chat.completions.create(
          model=model_name,  
          messages = [
                    {"role": "system", "content": "You are an expert Python programmer. You will be given a question (problem specification) and will generate a correct Python program that matches the specification. You will NOT return anything except for the program."},
                    {"role": "user", "content": prompt}
                ],
          max_tokens = 32768,
    )
 
    content = response.choices[0].message.content
    code = content 

    file_path = "./"+name_tail+"/py_code/"+name_tail+"_"+action+".py"

    try:
        with open(file_path, 'w') as f:
            f.write(code)
        print(f"✅ Successfully created and saved to '{file_path}'")
    except Exception as e:
        print(f"❌ An error occurred: {e}")



# fine-grained version
for action in tqdm(action_list): 
    for gender in gender_list:
        for happiness in happiness_list:
            for weight in weight_list:

                Question = "Question: write a Python program that shows a point-light stimulus animation which represents biological motion. \n Detailed Requirements: \n "

                prompt_action = "1. Subject and Action: The animation depict a "+ happiness + gender + " with " + weight +" weight is <" + action + ">. \n"

                prompt_style_quality = "2. Visual Style: The stimulus should consist of exactly 15 white point-lights moving against a solid black background. \n \
                  3. Motion Quality: The animation must be realistic, coherent, and biomechanically plausible to accurately represent the specified human action. The movement should be smooth and natural. \n"

                prompt = Question +prompt_action +prompt_style_quality 
                
                response = client.chat.completions.create(
                      model=model_name,   
                      messages = [
                                {"role": "system", "content": "You are an expert Python programmer. You will be given a question (problem specification) and will generate a correct Python program that matches the specification. You will NOT return anything except for the program."},
                                {"role": "user", "content": prompt}
                            ],
                      max_tokens = 32768,
                )
                
                content = response.choices[0].message.content
                code = content

                file_path = "./"+name_tail+"/py_code_fine/"+name_tail+"_"+gender+"_"+weight+"_"+happiness+"_"+action+".py"

                try:
                    with open(file_path, 'w') as f:
                        f.write(code)
                    print(f"✅ Successfully created and saved to '{file_path}'")
                except Exception as e:
                    print(f"❌ An error occurred: {e}")


