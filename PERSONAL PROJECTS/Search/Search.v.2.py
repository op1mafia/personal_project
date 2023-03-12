import webbrowser

#creat a variable for search and a any_word variable:
Search = input("The search is ...")
print("this is a results of ..." + Search)
webbrowser.open("https://www.youtube.com/results?search_query=" + Search)
