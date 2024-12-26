import os
import pandas as pd
from tqdm import tqdm


def extract_c_functions_from_lines(content):
    """
    Extract functions and clean them only if there are more than 2 functions.
    """
    # Split on triple newlines to separate functions
    functions = [f for f in content.split('\n\n\n')]
    
    # Only clean if we have more than 2 functions
    if len(functions) > 2:
        cleaned_functions = []
        for function in functions:
            # Check if function has any non-whitespace/newline content
            has_content = False
            for char in function:
                if char != ' ' and char != '\n':
                    has_content = True
                    break
            
            if has_content:
                cleaned_functions.append(function)
        return cleaned_functions
    
    return functions

def extract_functions_from_file_c(file_path, df):
    try:
        with open(file_path, 'r', encoding='utf-8') as file_:
            content = file_.read()
        
        functions = extract_c_functions_from_lines(content)
        
        if len(functions) > 2:
            print(f"Warning: {file_path} contains {len(functions)} valid functions instead of 2")
        
        if len(functions) >= 2:
            function1, function2 = functions[0], functions[1]
        else:
            print(f"Not enough functions in {file_path}")
            function1, function2 = None, None
        
        # Add the row to dataframe only if we have valid functions
        if function1 is not None and function2 is not None:
            df.loc[len(df.index)] = [file_path, function1, function2]
        
        return df
    except Exception as e:
        print(f"Error processing {file_path}: {str(e)}")
        return df
def process_language_files(base_path, folders_paths, file_extension, output_filename):
    """Process all files for a specific language"""
    print(f"\nProcessing {file_extension} files...")
    
    df = pd.DataFrame(columns=["filename", "function 1", "function 2"])
    
    for folder in folders_paths:
        full_path = os.path.join(base_path, folder.lstrip('/'))
        if os.path.exists(full_path):
            # Walk through directory to find .c files
            for root, _, files in os.walk(full_path):
                for file in files:
                    if file.endswith(file_extension):
                        file_path = os.path.join(root, file)
                        df = extract_functions_from_file_c(file_path, df)
    
    print(f"Total {file_extension} files processed successfully: {len(df)}")
    df.to_csv(output_filename, index=False)
    return df



if __name__ == "__main__":

    base_path = "./GPTCloneBench/standalone/true_semantic_clones"
    folders_paths = ["/py/prompt_1/MT3","/py/prompt_1/T4","/py/prompt_2/MT3","/py/prompt_2/T4"]

    '''
    # For false Semantics
    base_path = "./GPTCloneBench/standalone/false_semantic_clones"
    folders_paths = ["/py/"]

    '''
    paths = [os.path.abspath(base_path + f) for f in folders_paths]

    df = pd.DataFrame(columns=["filename", "function 1", "function 2"])
    
    for p in tqdm(paths):
        df = process_language_files(base_path, folders_paths, '.py', "true_positive_python.csv")
            
    print(f"\nTotal files processed successfully: {len(df)}")
    df.to_csv("true_positive_python.csv", index=False)