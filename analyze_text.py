# Remember to reach out for help after your own due diligence

def analyze_text(text):
    # Your code here
    
    alpha_counter = 0
    e_num_counter = text.count("e") + text.count("E")
    e_percent = 0
    
    for letter in text: 
        if letter.isalpha():
            alpha_counter += 1
        else:
            alpha_counter += 0 
       
    if e_num_counter > 0:
        e_percent = 100 * (e_num_counter / alpha_counter)
       
    e_percent = "{:0.2f}".format(e_percent)
    return "The text contains " + str(alpha_counter) + " alphabetic characters, of which " + str(e_num_counter) + " (" + str(e_percent) + "%) are 'e'."

