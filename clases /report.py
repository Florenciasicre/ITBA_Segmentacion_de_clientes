import webbrowser 
class GetHtml:
    def __init__(self, data): 
       self.info = data
    def create_HTML(self):
        with open('output.html', 'w') as html_file:
        # the html code which will go in the file GFG.html
          html_template = "<!DOCTYPE html>\n<html>\n\t<head></head>\n\t<body>"
          html_template += "<table><tr>"
          html_template += "</body>\n</html>"
          # writing the code into the file
          html_file.write(html_template)
            
          # close the file
      
          
        webbrowser.open('GFG.html') 
