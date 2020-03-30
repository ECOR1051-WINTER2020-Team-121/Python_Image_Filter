import Cimpl
from T121_image_filters import * 

def load()-> Cimpl.Image:
    """ The author: Ibrahim Kasim
    prompts the user to choose an image object,then loads that image to the variable
    called image_selected. Then, It displays the image. 

    >>>load()
    -> displays the Cimpl.Image  
    """
    var1 = Cimpl.choose_file() 
    image_selected = Cimpl.load_image(var1)
    Cimpl.show(image_selected)
    return image_selected

def save_as(image_selected:Cimpl.Image) -> None:
    """ The author: Ibrahim Kasim
    selected image object passed as an argument, then it prompts user to type 
    their preferred name for the file to be saved as. 
    
    >>>save_as(an_image_object)
    ...please type the name of the file you want to save your image as: funny_pic.png
    
    """
    print("please type the name of the file you want to save your image as:", end ="")
    name_image = str(input()) 
    Cimpl.save_as(image_selected, name_image)

def threshold_value()-> int:
    """ The author: Ibrahim Kasim
    prompts the user to type in their preferred threshold value as integer. Returns
    an integer value.

     >>>threshold_value()
     ...please type the threshold value of the filter you want to apply to your image:4
    """
    print("please type the threshold value of the filter you want to apply to your image:",end = "")
    threshold_int = int(input())   
    return threshold_int


def print_menu()-> str:
    """ The author: Ibrahim Kasim
    returns a series of strings. These strings make up the main menu of 
    the program. 
    """
    print("{}  {}".format("L)oad)","S)ave-as"))
    print("{}  {}  {}".format("2)-tone","3)-tone","X)treme contrast"),end = "")
    print(" {}  {}".format("T)int sepia","P)osterize"))
    print("{}  {}  {}".format("E)dge detect","I)mproved edge detect","V)ertical flip"),end="")
    print("  {}".format("H)orizontal flip"))
    print("{}".format("Q)uit"))
    print("")
    

def loop_commands(selected_option:str)->bool:  
    """ The author: Ibrahim Kasim
    returns true or false depending on whether user input is matching any of the
    acceptable commands of the program. 
    >>>loop_commands("asd")
    ...False
    >>>loop_commands("t)")
    ...True 
    """
    acceptable_commands = ["q)","Q)","2)","3)","l)","L)","s)","S)","x)","X)","t)","T)","P)","p)",
                           "e)","E)","i)","I)","v)","V)","h)","H)"]
    count_acceptable = 0
    for command in acceptable_commands:
        if command == selected_option:
            count_acceptable += 1
    if count_acceptable == 0:
        return False                     
    else:
        return True      

def main()-> Cimpl.Image:
    """ The author: Ibrahim Kasim 
    It is a complex, user interactive program to apply filters to the user input object images.
    the available commands are displayed as program menu at the start. if exit command 
    chosen, it exists the program. If any particular filter applied, it returns an object image. 
    The program is cumulative as user can apply one filter on top of other. 

    >>>main()
    ...please type an option:e)
    ...-> Cimpl.Image
    >>>main()
    ...please type an option:Q)
    ...program exited.
    >>>main()
    ...please type an option:asd
    ...no such command
    
    if user typed a valid command before loading an image: 
    
    >>>main()
    ...please type an option:
    ...no image loaded
    """
    # image_selected has to be initialized to ensure that user does not make a selection before
    # loading an image. Otherwise, error is raised.
    image_selected = 0
    # a test variable to check whether the command is the exit command, is needed. 
    # selected_option represents the string typed by the user, in order to use it 
    # inside of the while loop condition, it must be initialized.
    test_variable = 0 
    
    while test_variable == 0:
        
        print_menu()
        
        print("please type an option:",end="")
        selected_option = str(input())
        selected_option = selected_option.upper() + ")"

        if selected_option == "L)":
            image_selected = load()

        elif selected_option == "S)" and image_selected != 0:
            save_as(image_selected)

        #elif selected_option == "2)") and image_selected != 0:
            #print("please type the")
            #image_selected = two_tone(image_selected,,)
            #Cimpl.show(image_selected)
        
        #elif selected_option == "3)" and image_selected != 0:
            #image_selected = three_tone(image_selected,,,)
            #Cimpl.show(image_selected)
        
        elif  selected_option == "X)" and image_selected != 0:
            image_selected = extreme_contrast(image_selected)
            Cimpl.show(image_selected)
        
        elif selected_option == "T)" and image_selected != 0:
            image_selected = sepia(image_selected)
            Cimpl.show(image_selected)
        
        elif selected_option == "P)"  and image_selected != 0:
            image_selected = posterize(image_selected)
            Cimpl.show(image_selected)
        
        elif  selected_option == "E)" and image_selected != 0: 
            image_selected = detect_edges(image_selected,threshold_value())
            Cimpl.show(image_selected)
        
        elif selected_option == "I)" and image_selected != 0:
            image_selected = detect_edges_better(image_selected,threshold_value())
            Cimpl.show(image_selected)
        
        elif selected_option == "V)" and image_selected !=0: 
            image_selected = flip_vertical(image_selected)
            Cimpl.show(image_selected)
        
        elif selected_option == "H)" and image_selected != 0: 
            image_selected = flip_horizontal(image_selected)
            Cimpl.show(image_selected)
        test_variable = 0
        
        if selected_option == "Q)":
            test_variable = 1
        command_check = loop_commands(selected_option)
        
        if command_check == False:
            print("no such command")
        elif (command_check == True) and test_variable == 0 and image_selected == 0:
            print("no image loaded")
        
    
    print("program exited.")

main()