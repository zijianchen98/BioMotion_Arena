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

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


model_name = "xxxxxxx"
name_tail = "xxxx"

base64_image1 = encode_image('./ref.png')


action_list = ['walking']  # ,'running', 'waving a hand', 'jumping up', 'jumping forward', 'bowing', 'lying down', 'sitting down', 'turning around', 'forward rolling']

gender_list = ['man','woman']

happiness_list = ['happy','sad']

weight_list = ['heavy', 'light']

points= ['15']

for i in range(3):

  for action in tqdm(action_list): 
    for point in points:
      Question = "Question: Given an example image <image>, write a Python program that shows a point-light stimulus animation which represents biological motion. \n Detailed Requirements: \n "

      prompt_action = "1. Subject and Action: The animation depict a man is <" + action + ">. \n"

      prompt_style_quality = "2. Visual Style: The stimulus should consist of exactly "+ point+ " white point-lights moving against a solid black background. \n 3. Motion Quality: The animation must be realistic, coherent, and biomechanically plausible to accurately represent the specified human action. The movement should be smooth and natural. The style should be the same as the example image. \n"

      prompt = Question + prompt_action +prompt_style_quality
      
      response = client.chat.completions.create(
            model=model_name,   
            messages=[
              {"role": "system", "content": "You are an expert Python programmer. You will be given a question (problem specification) and will generate a correct Python program that matches the specification and passes all tests. You will NOT return anything except for the program."},
              {
                "role": "user",
                "content": [
                  {
                    "type": "text",
                    "text": prompt
                  },
                  {
                    "type": "image_url",
                    "image_url": {
                      "url": f"data:image/png;base64,{base64_image1}"
                    },

                  }
                ]
              }
            ],
            max_tokens = 32768,
      )

      content = response.choices[0].message.content
      print(content)
      
      match = re.search(r'```python(.*?)```', content, re.DOTALL)
      if match:
          code = match.group(1)



      file_path = "./"+name_tail+"/py_code/"+name_tail+"_"+action+"_point_"+point+"-"+str(i)+".py"
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

                Question = "Question: Given an example image <image>, write a Python program that shows a point-light stimulus animation which represents biological motion. \n Detailed Requirements: \n "

                prompt_action = "1. Subject and Action: The animation depict a "+ happiness + gender + " with " + weight +" weight is <" + action + ">. \n"

                prompt_style_quality = "2. Visual Style: The stimulus should consist of exactly 15 white point-lights moving against a solid black background. \n \
                  3. Motion Quality: The animation must be realistic, coherent, and biomechanically plausible to accurately represent the specified human action. The movement should be smooth and natural. The style should be the same as the example image. \n"

                prompt = Question +prompt_action +prompt_style_quality 
                
                response = client.chat.completions.create(
                model=model_name,  
                messages=[ 
                        {"role": "system", "content": "You are an expert Python programmer. You will be given a question (problem specification) and will generate a correct Python program that matches the specification and passes all tests. You will NOT return anything except for the program."},
                        {
                          "role": "user",
                          "content": [
                            {
                              "type": "text",
                              "text": prompt
                            },
                            {
                              "type": "image_url",
                              "image_url": {
                                "url": f"data:image/png;base64,{base64_image1}"
                              },

                            }
                          ]
                        }
                      ],
                      max_tokens = 32768,
                )
                
                content = response.choices[0].message.content
                
                match = re.search(r'```python(.*?)```', content, re.DOTALL)
                if match:
                    code = match.group(1)
                   


                file_path = "./"+name_tail+"/py_code_fine/"+name_tail+"_"+gender+"_"+weight+"_"+happiness+"_"+action+".py"

                try:
                    with open(file_path, 'w') as f:
                        f.write(code)
                    print(f"✅ Successfully created and saved to '{file_path}'")
                except Exception as e:
                    print(f"❌ An error occurred: {e}")


