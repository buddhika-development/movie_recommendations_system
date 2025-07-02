import requests


def embedding_function(text):
    """
    Create text embeddings

    does:
        this function is responsible for create embeddings of the texts

    args:
        text content neet convert into vector values
    
    return:
        if text exits return the embedding othewise return the None
    """


    try:
        response = requests.post(
            "http://127.0.0.1:11435/api/embeddings",
            json = {
                "model" : "nomic-embed-text:latest",
                "prompt" : text
            }
        )

        if response.status_code == 200:
            json_response = response.json()
            embedding = json_response["embedding"]
        
            if embedding:
                return embedding
            else:
                return None
    except Exception as e:
        print(f"Something went wrong in the model connection... {e}")
        return None