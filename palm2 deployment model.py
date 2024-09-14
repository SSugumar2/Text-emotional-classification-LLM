import google.generativeai as palm

def configure_palm(api_key):
    palm.configure(api_key=api_key)

def generate_text(api_key, prompt):
    configure_palm(api_key)
    models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
    model = models[0].name
    try:
        completion = palm.generate_text(model=model, prompt=prompt, max_output_tokens=50)
        if completion and completion.result:
            return completion.result.strip()
        else:
            return "Error: No result returned from the model."
    except Exception as e:
        return f"Error: {str(e)}"
