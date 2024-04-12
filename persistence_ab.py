# Package per salvare e rileggere il file su github
from github import Github
import pickle


def upload_file(df,repository_name, username, token, file_path):
    encoded_data = pickle.dumps(df)
    # GitHub authentication
    g = Github(username,token)
    # Get repository
    try:
        repo = g.get_user().get_repo(repository_name)
    except Exception as e:
        print("Error accessing repository:", e)
        exit()
    file = repo.get_contents(file_path)
    repo.update_file(file_path, "Updated data", encoded_data, file.sha)
    print("File updated successfully.")

def retrieve_file(repository_name, username,token, file_path):
    g = Github(username,token)

    # Get repository
    try:
        repo = g.get_user().get_repo(repository_name)
    except Exception as e:
        print("Error accessing repository:", e)
        exit()
    contents = repo.get_contents(file_path)
    content_string = contents.decoded_content
    loaded_data = pickle.loads(content_string)
    
    return loaded_data
