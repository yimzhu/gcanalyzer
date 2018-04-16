#!/usr/bin/env python    
#encoding: utf-8  
import ctypes  
  
STD_INPUT_HANDLE = -10  
STD_OUTPUT_HANDLE= -11  
STD_ERROR_HANDLE = -12  
  
FOREGROUND_BLACK = 0x0  
FOREGROUND_BLUE = 0x01 # text color contains blue.  
FOREGROUND_GREEN= 0x02 # text color contains green.  
FOREGROUND_RED = 0x04 # text color contains red.  
FOREGROUND_INTENSITY = 0x08 # text color is intensified.  
  
BACKGROUND_BLUE = 0x10 # background color contains blue.  
BACKGROUND_GREEN= 0x20 # background color contains green.  
BACKGROUND_RED = 0x40 # background color contains red.  
BACKGROUND_INTENSITY = 0x80 # background color is intensified.  
  
class Color:  
    ''''' See http://msdn.microsoft.com/library/default.asp?url=/library/en-us/winprog/winprog/windows_api_reference.asp 
    for information on Windows APIs.'''  
    std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)  
      
    def set_cmd_color(self, color, handle=std_out_handle):  
        """(color) -> bit 
        Example: set_cmd_color(FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_BLUE | FOREGROUND_INTENSITY) 
        """  
        bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)  
        return bool  
      
    def reset_color(self):  
        self.set_cmd_color(FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_BLUE)  
      
    def print_red_text(self, print_text):  
        self.set_cmd_color(FOREGROUND_RED | FOREGROUND_INTENSITY)  
        print print_text  
        self.reset_color()  
          
    def print_green_text(self, print_text):  
        self.set_cmd_color(FOREGROUND_GREEN | FOREGROUND_INTENSITY)  
        print print_text  
        self.reset_color()  
      
    def print_blue_text(self, print_text):   
        self.set_cmd_color(FOREGROUND_BLUE | FOREGROUND_INTENSITY)  
        print print_text  
        self.reset_color()  
            
    def print_red_text_with_blue_bg(self, print_text):  
        self.set_cmd_color(FOREGROUND_RED | FOREGROUND_INTENSITY| BACKGROUND_BLUE | BACKGROUND_INTENSITY)  
        print print_text  
        self.reset_color()      
  
if __name__ == "__main__":  
    table = Texttable()
    table.set_cols_align(["l", "r", "c"])
    table.set_cols_valign(["t", "m", "b"])
    table.add_rows([["Name", "Age", "Nickname"],
                ["Mr\nXavier\nHuon", 32, "Xav'"],
                ["Mr\nBaptiste\nClement", 1, "Baby"]])
    print(table.draw() + "\n")
    table = Texttable()
    table.set_deco(Texttable.HEADER)
    table.set_cols_dtype(['t',  # text
                      'f',  # float (decimal)
                      'e',  # float (exponent)
                      'i',  # integer
                      'a']) # automatic
    table.set_cols_align(["l", "r", "r", "r", "l"])
    table.add_rows([["text",    "float", "exp", "int", "auto"],
                ["abcd",    "67",    654,   89,    128.001],
                ["efghijk", 67.5434, .654,  89.6,  12800000000000000000000.00023],
                ["lmn",     5e-78,   5e-78, 89.4,  .000000000000128],
                ["opqrstu", .023,    5e+78, 92.,   12800000000000000000000]])
    print(table.draw())
    clr = Color()  
    clr.print_red_text('red')  
    clr.print_green_text('green')  
    clr.print_blue_text('blue')  
    clr.print_red_text_with_blue_bg('background')  