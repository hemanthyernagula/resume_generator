from flask import Flask, render_template


app = Flask(__name__)


right_arrow_icon = """<svg xmlns='http://www.w3.org/2000/svg' width='16' height='16' fill='currentColor' class='bi bi-arrow-right-short' viewBox='0 0 16 16'>
    <path fill-rule='evenodd' d='M4 8a.5.5 0 0 1 .5-.5h5.793L8.146 5.354a.5.5 0 1 1 .708-.708l3 3a.5.5 0 0 1 0 .708l-3 3a.5.5 0 0 1-.708-.708L10.293 8.5H4.5A.5.5 0 0 1 4 8z'/>
  </svg>"""
  
my_content = {
    "header":{
        "title": {
        "type": "text",
        "value": "Hemanth Yernagula"
    },
        "contact_info":{
            "non_clickable": [
                (9353463551, """<svg xmlns='http://www.w3.org/2000/svg' width='10' height='10' fill='currentColor' class='bi bi-phone-fill' viewBox='0 0 16 16'>
    <path d='M3 2a2 2 0 0 1 2-2h6a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V2zm6 11a1 1 0 1 0-2 0 1 1 0 0 0 2 0z'/>
  </svg>"""),
                ("yernagulahemanth@gmail.com", """<svg xmlns='http://www.w3.org/2000/svg' width='10' height='10' fill='currentColor' class='bi bi-envelope-fill' viewBox='0 0 16 16'>
    <path d='M.05 3.555A2 2 0 0 1 2 2h12a2 2 0 0 1 1.95 1.555L8 8.414.05 3.555zM0 4.697v7.104l5.803-3.558L0 4.697zM6.761 8.83l-6.57 4.027A2 2 0 0 0 2 14h12a2 2 0 0 0 1.808-1.144l-6.57-4.027L8 9.586l-1.239-.757zm3.436-.586L16 11.801V4.697l-5.803 3.546z'/>
  </svg>""")
            ],
        
            "click_able": [
                ("https://www.linkedin.com/in/hemanth-yernagula", """<svg xmlns='http://www.w3.org/2000/svg' width='10' height='10' fill='currentColor' class='bi bi-linkedin' viewBox='0 0 16 16'>
                    <path d='M0 1.146C0 .513.526 0 1.175 0h13.65C15.474 0 16 .513 16 1.146v13.708c0 .633-.526 1.146-1.175 1.146H1.175C.526 16 0 15.487 0 14.854V1.146zm4.943 12.248V6.169H2.542v7.225h2.401zm-1.2-8.212c.837 0 1.358-.554 1.358-1.248-.015-.709-.52-1.248-1.342-1.248-.822 0-1.359.54-1.359 1.248 0 .694.521 1.248 1.327 1.248h.016zm4.908 8.212V9.359c0-.216.016-.432.08-.586.173-.431.568-.878 1.232-.878.869 0 1.216.662 1.216 1.634v3.865h2.401V9.25c0-2.22-1.184-3.252-2.764-3.252-1.274 0-1.845.7-2.165 1.193v.025h-.016a5.54 5.54 0 0 1 .016-.025V6.169h-2.4c.03.678 0 7.225 0 7.225h2.4z'/>
                </svg>"""),
                ("https://github.com/hemanthyernagula", """<svg xmlns='http://www.w3.org/2000/svg' width='10' height='10' fill='currentColor' class='bi bi-github' viewBox='0 0 16 16'>
                  <path d='M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.012 8.012 0 0 0 16 8c0-4.42-3.58-8-8-8z'/>
                  </svg> """)
            ],
            }
    },
    "body": {
        "block1":{
            "align": "element-left",
            "style_width": "width: 100%;",
            "type": "introduction",
            "title": "Executive Summary",
            "value": """Experienced NLP professional with 3 years of expertise in advanced NLP models, including Attention
            Mechanism, proficient in leveraging HuggingFace pretrained models for fine-tuning llms using PEFT concepts.
            Skilled in data extraction, manipulation, and preparation using Python libraries like Pandas and regular
            expressions. Automates tasks, generates analytical reports, and schedules emails with crontab. Creates
            efficient data pipelines using PyTorch data loaders for training and testing neural network models.
            Experienced in building Flask APIs around ML/DL models and containerizing applications with Docker for
            seamless deployment. Additional experience includes integrating Asterisk PBX with real-time SIP connections
            and leveraging Python AGI for NLP techniques to understand speech in call scenarios.""",
        },
        "block2":{
            "align": "element-left",
            "type": "experience",
            "title": "Experience",
            "value": [
                {
                    "company_name": "Gnani Ai",
                    "period": "Nov 2020 to April 2024",
                    "projects": [{
                        "title": 'Agent Assistant',
                        "aspects": [
                            ("Prompt fine tuning to get desired output from LLM's", right_arrow_icon),
                            ("Comparing the results from different model outputs.", right_arrow_icon),
                            ("Preparing data for fine-tuning LLM's.", right_arrow_icon),
                            ("Lora, QLora fine-tuning.", right_arrow_icon),
                            ("Containerizing the finetuned model for deployment.", right_arrow_icon),
                            ("Tracking the model with the frameworks like MLFlow.", right_arrow_icon)
                        ]
                        },
                        {
                        "title": "Inverse Text Normalization(ITN)",
                        "aspects": [                        
                                    ("Writing Python code to generate data that is appropriate for ITN model.", right_arrow_icon),
                                    ("Training ITN model with generated data.", right_arrow_icon),
                                    ("Post processing the results of the ITN model predictions", right_arrow_icon),
                                    ("Observing results of the model and making required changes in the data to train robust ITN model.", right_arrow_icon),
                                    ("Creating the image and containerizing the application using docker.", right_arrow_icon),
                        ]
                    },
                        {
                        "title": "Voice Bot(Appointment Scheduler)",
                        "aspects": [
                            ("Creating conversation flows on the prototype provided by the client.", right_arrow_icon),
                            ("Creating data validations to ensure the quality of the data and hitting email alerts if any improper values observed on data fields with python.", right_arrow_icon),
                            ("Date manipulation and validations on the date provided by the customer on call using python.", right_arrow_icon),
                            ("Observing the conversation data and drawing insights to make decisions on improvements on existing flow of the bot.", right_arrow_icon)
                        ]
                        
                        },
                        
                    ]
                }
            ]
        },
        "block3":{
            "align": "element-right",
            "type": "skills",
            "title": "Skills",
            "value": [
                {
                    "Machine Learning":{
                    "align": "left-obj",
                    "details":[
                    ("KNN", right_arrow_icon),      
                    ("Logistic Regression", right_arrow_icon),      
                    ("Linear Regression", right_arrow_icon),      
                    ("SVM", right_arrow_icon),      
                    ("Ensemble Models", right_arrow_icon),  
                    ],},

                    "NLP Techniques":{
                    "align":"right-obj",
                    "details":[
                    ("Lora Fine Tuning", right_arrow_icon),      
                    ("Model Quantization", right_arrow_icon),      
                    ("RAG Operations", right_arrow_icon),      
                    ("Prompt Fine Tuning", right_arrow_icon),  
                    ]},

                    "Python Libraries":{
                    "align":"left-obj",
                    "details":[
                    ("SKLearn", right_arrow_icon),      
                    ("Pandas", right_arrow_icon),      
                    ("PyTorch", right_arrow_icon),      
                    ("Flask", right_arrow_icon),      
                    ("Rasa", right_arrow_icon),  
                    ]},

                    "Tools":{
                    "align":"right-obj",
                    "details":[
                    ("Jupyter Notebook", right_arrow_icon),      
                    ("VsCode", right_arrow_icon),      
                    ("Git", right_arrow_icon),      
                    ("Docker", right_arrow_icon),      
                    ("MongoDb", right_arrow_icon),
                    ]},
                }
            ]
        }
    }
}

@app.route('/')
def home():
    return render_template('home.html', data=my_content)

    

if __name__ == '__main__':
    app.run(host="localhost",debug=True,)

