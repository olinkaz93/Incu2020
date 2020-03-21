def getInterfaces():

    try:
        file = open(
            r"C:\Users\Ola\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.8\mongo_flask_homework\text\interface2.txt",
            "rt", encoding="utf8")
        #dictionary = {}
        #ln = 0
        #allSwitches = []
        allInterfaces = []

        for line in file:
            if (line == '\n'):
                continue

            #if (line.startswith('Switch')):
            #    print("Switch", line)
            #if (line.startswith('\t')):
            #    print("Interface", line)
            #if (line.startswith('con')):
            #    print("Description", line)
            #line stores string. line[1] shows the letter at [1] index in this line
            #print("number line:", ln, "whole line", line)
            # number of lines in document: ln
            #ln = ln + 1

            #make a list of elements from line of document, seprator is ","
            x = line.split(",")
            #for i in x:
                    #print("Printing elements in X", i)

            #dictionary of Interface
            keysInterface = ['Interface_Name', 'Description', 'State']
            interface = {}

            #dictionary of Switch
            #switch = {}
            keysSwitch = ['Switch_Type']

            #each element in x : each of them 'i' in the list of x
            for i in x:
                #to remove blank spaces from the item
                data=i.strip()
                if (data.startswith('Switch')):
                    #assign Switch as a new 'Switch_Type' in dictionary switch
                    #switch[keysSwitch[0]] = data
                    #append switch dictionary with details to allSwitches list
                    #allSwitches.append(switch)
                    dataSwitch = data.strip(":")
                    currentSwitch = dataSwitch

                elif (data.startswith('int')):
                    #append interface dictionary with details to allInterface list
                    allInterfaces.append(interface)
                    # assign currentSwitch as a 'Switch_Type'' in dictionary interface
                    interface[keysSwitch[0]] = currentSwitch
                    # assign Interface as a new 'Interface_Name' in dictionary interface
                    interface[keysInterface[0]] = data
                    #print("Current interfaces", interface, "current switch", currentSwitch)
                elif (data.startswith('Connected', 1)) or (data.startswith('connected', 1)):
                    # assign Interface Describe as a new 'Description' in dictionary interface
                    interface[keysInterface[1]] = data
                    #print("Current interfaces", interface)
                elif (data.startswith('up') or data.startswith('down')):
                    # assign Interface State as a new 'State' in dictionary interface
                    interface[keysInterface[2]] = data
                    #print("Current interfaces", interface)


        #print("**************RESULT*****************")
        #print("List of switches", allSwitches)
        #print("Switch 1", allSwitches[0])
        #print("List of interfaces", allInterfaces)
        #print("Interface 1", allInterfaces[0])
        #print("type of data int 1", type(allInterfaces[0]), allInterfaces[0])

        """
        for elem in allInterfaces:
            print("elem in interface", elem)
            for key in elem:
                print("key in elem", key, "element of that key", elem[key])
    
        for elem in allSwitches:
            print("elem in switch", elem)
            for key in elem:
                print("key in elem", key, "element of that key", elem[key])
        """

            #print("i to: ", i, "data to: ", data)
            #print("Line x", x, "Interface", interfaces)
            #print("Line x", x, "Switches", switches)
            #print("this is list of string", x, len(x), x[0])

            #x = line.split(" ")
            #print(x)
            #print(x[0])

        result = allInterfaces

        file.close()
    except Exception as exc:
        print("Cannot open the file:", exc)

    #print("*******************Final result*****************", result)

    return result

#print(getInterfaces())
#print("Interaces in the file", getInterfaces())