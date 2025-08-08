NOTE FINISH THIS WHEN IM DONE

At a high level this project is designed to take in a folder of folders (the subfolders representing clients, vendors, etc)

For each folder it does the following:
    1. Walk through the whole folder
    2. Take out ALL the text
    3. Insert the text into a prompt     **NOTE: the prompt MUST request a json response**
    4. The prompt is passed to Perplexity
    5. Each JSON attribute is placed in an excel column in a desired excel sheet

    *If this is the first subfolder that is being processed, an excel sheet with corresponding columns will automatically be generated*