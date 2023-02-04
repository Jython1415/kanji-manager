import shutil
import math

class ShoeMenu():
    
    def __init__(self, title):
        self.description = ""
        self.title = title
        self.prologueText = ""
        self.epilogueText = ""
        
        # List of options
        # Each option should be a tuple (listOrder, name, function)
        self.options = list()
    
    @staticmethod
    def genLeftJustifiedLine(text, consoleWidth=shutil.get_terminal_size().columns) -> str:
        return text.join(" " * (consoleWidth-len(text)))
    
    @staticmethod
    def optionsKey(options):
        return options[0]
    
    def addOptions(self, options):
        for option in options:
            self.options.append(option)
        self.options.sort(key=ShoeMenu.optionsKey)
        
    def generateOptions(self):
        content = ""
        i = 0
        for option in self.options:
            i += 1
            content.join(ShoeMenu.genLeftJustified(str(i).zfill(int(math.log10(len(self.options))) + 1).join(" ", option[1])), "\n")
        
        return(content)
            
    # Progress bar
    # Code from Ivan Procopovich on StackOverflow
    def print_percent_done(index, total, bar_len=50, title='Please wait'):
        '''
        index is expected to be 0 based index. 
        0 <= index < total
        '''
        percent_done = (index+1)/total*100
        percent_done = round(percent_done, 1)

        done = round(percent_done/(100/bar_len))
        togo = bar_len-done

        done_str = '█'*int(done)
        togo_str = '░'*int(togo)

        print(f'\t⏳{title}: [{done_str}{togo_str}] {percent_done}% done', end='\r')

        if round(percent_done) == 100:
            print('\t✅')
