

def get_prompt(job_url) : 
    file_path = "llm/prompt"

    with open(file_path, "r") as file:
        content = file.read()

    content = content.replace("<job link>", job_url)
    return content

if __name__ == "__main__" :
    print(get_prompt("https://jobs.apple.com/en-us/details/200601603/python-developer"))