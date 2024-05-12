# local_gpt
Ready to deploy Offline LLM AI web chat.

## Usage
Instructions to install all the required software and settings.

1. Install Torch from the [official site](https://pytorch.org/get-started/locally/), for more performance use the cuda version if you have the needed hardware.  

2. Clone this repository  
```bash
    git clone --recurse-submodules https://github.com/ubertidavide/local_gpt.git
```

2. Install all Python dependencies using pip:  
```bash
    pip install -r requirements.txt
```

3. Insert your preferred prompt at `line 24` in the `main.py` code, you could found some awasome promts [here](https://github.com/f/awesome-chatgpt-prompts)  

4. Deploy the app locally:  
```bash
    streamlit run main.py
```