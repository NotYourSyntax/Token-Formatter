import os

def clean_token_file(input_file='tokens.txt', output_file='cleaned_tokens.txt'):
    """Extracts bare tokens from potential email:password:token combinations"""
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found")
        return
        
    cleaned = []
    total = 0
    
    with open(input_file, 'r') as infile:
        for line in infile:
            line = line.strip()
            if not line:
                continue
                
            
            token = line.split(':')[-1].strip()
            
           
        if token.count('.') == 2 and len(token) > 30:
                cleaned.append(token)
                total += 1
    
    if not cleaned:
        print("No valid tokens found")
        return
    
    with open(output_file, 'w') as outfile:
        outfile.write("\n".join(cleaned))
    
    print(f"Success! {total} tokens saved to {output_file}")
    print("Warning: Treat these tokens like passwords - never share them!")

if __name__ == "__main__":
    print("Discord Token Cleaner v2.0")
    print("Simply removes email:password prefixes while keeping full tokens\n")
    
    input("Press Enter to process tokens.txt...")
    clean_token_file()
