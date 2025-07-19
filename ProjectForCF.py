
from tkinter import *

root = Tk()


#Linear Search
#starts from first index and keeps prgressing throught the array and finds the element
#return -1 is like else
def linear_search(array, x):
    for i in range(len(array)):
        if array[i] == x:
            return i
    return -1
#starting 2-3 lines are getting item we want to search from entry box
#line 205 we are getting array
#in 3rd one we need to apply for loop on array to search
#line 210 we apllay if else
#
def on_search():
  search_item = int(search_entry.get())
  arr = entry.get().split(",")
  arr = [int(i) for i in arr]#for loop used here
  result = linear_search(arr, search_item)
  if result != -1:
      result_label.config(text=f"Item found at index {result}")
  else:
      result_label.config(text="Item not found")

#-----------------------------------------------------------------

#Binary Search
#In binary search, it finds the middle element and compares the element. If it is middle element, it returns it.
#if it is greater then middle element it knows that element is on right side and applies same thing.
#Same thing for left. It keeps doing untill finds it
#this functioin finds the middle value after sorting and find if num is bigger than goes to the right side and finds the middle of that and...
      
def binary_search(arr, x):
  #starting point
  low = 0
  #ending point
  #find last number it can be
  high = len(arr) - 1
  mid = 0
  while low <= high:
      mid = (high + low) // 2
      if arr[mid] < x:
          low = mid + 1
      elif arr[mid] > x:
          high = mid - 1
      else:
          return mid
  return -1
#same as other ones like this
def on_search_binary():
  search_item = int(search_entry.get())
  arr = entry.get().split(",")
  arr = [int(i) for i in arr]
  arr.sort()
  result = binary_search(arr, search_item)
  if result != -1:
      result_label.config(text=f"Item found at index {result}")
  else:
      result_label.config(text="Item not found")



#-------------------------------------------------------------------------------
#here first find the low and high value and check if they are equal and also check if low is equal to x which we are looking for then it will return a no.
#otherwise a mid value we will find out mid value using given formula in pos variable. then use if then to compare value with pos and pos with others nos
#if the starting value is same as what we are seraching for, than dont have to go further
#not done in inary search
#in interppolation very similar to binary
#first sort array, use if then to check if starting value is sama as what we are searching for, if gets value, good, otherwise goes further
#here we use a position to compare iwth what we are searchign for rather than middle position
#we use formula
#in this we find position using interpolation formuka and that position is being compared when we move to left and right side
#dont find middle value
#INTERPolatin formula used t find specific position
def interpolation_search(arr, x):
  low = 0
  high = len(arr) - 1
  while low <= high and x >= arr[low] and x <= arr[high]:
      if low == high:
          if arr[low] == x:
              return low
          return -1
      pos = low + int(((float(high - low) /
          (arr[high] - arr[low])) * (x - arr[low])))
      if arr[pos] == x:
          return pos
      if arr[pos] < x:
          low = pos + 1
      else:
          high = pos - 1
  return -1
#same
def on_search_interpolation():
  search_item = int(search_entry.get())
  arr = entry.get().split(",")
  arr = [int(i) for i in arr]
  arr.sort()
  result = interpolation_search(arr, search_item)
  if result != -1:
      result_label.config(text=f"Item found at index {result}")
  else:
      result_label.config(text="Item not found")

# Print the index where 'x' is located

#-----------------------------------------------------------------------------------------
#Exponential Search
#little bit similar to binary search in terms of comparing becasue caomparing to left side and right side
#sort, then chek if starting element is same as what we are searching for
#in this, we find middle value and compare
#here w edouble thei value
#i is the elment with which we are comparing x
#in binary , no if in beh=ginnihg
#ew also double i value i is the value with which we arfe  comparing x
#formula is same as in binary search
#expomnetial is combo of imterpolatio and binary
#we doubled because in the loop each and every value will be doubled and it will 
#in order to find out the range of a value, we start form the staring value 1 and compares it with the last element x
#once we get the index value i after doubling of i, we take the power of each and evry element becasue exponnetila search is called as doubling search
#where you take the peower 2 of the lower and upper values
def exponential_search(arr, x):
  if arr[0] == x:
      return 0
  i = 1
  while i < len(arr) and arr[i] <= x:
      i = i * 2
  return exponential2_search(arr, x, i // 2, min(i, len(arr)))
def exponential2_search(arr, x, start, end):
  while start <= end:
      mid = start + (end - start) // 2
      if arr[mid] < x:
          start = mid + 1
      elif arr[mid] > x:
          end = mid - 1
      else:
          return mid
  return -1
def on_search_exponential():
  search_item = int(search_entry.get())
  arr = entry.get().split(",")
  arr = [int(i) for i in arr]
  arr.sort()
  result = exponential_search(arr, search_item)
  if result != -1:
      result_label.config(text=f"Item found at index {result}")
  else:
      result_label.config(text="Item not found")



#call all functions here below on button in submit
#--------------------------------------------------------------------------------
def submit():
  if OM.get() == 'Linear Search':
    search_button.config(command=on_search)
    
  if OM.get() == 'Binary Search':
    search_button.config(command=on_search_binary)
    
  if OM.get()=="Interpolation Search":
    search_button.config(command=on_search_interpolation)
    
  if OM.get()=="Exponential Search":
    search_button.config(command=on_search_exponential)

  


root.title("Linear Search")
root.geometry("400x200")
title = Label(root, text = "Searching App")
title.grid(row = 0, column =0)
list=["Linear Search", "Binary Search","Interpolation Search", "Exponential Search"]
OM=StringVar(root)
OM.set("Searching Techniques")
menu = OptionMenu(root, OM,*list)
menu.grid(row = 2, column = 0)

instruction = Label(root, text ="Select the searching technique below:")
instruction.grid(row = 1, column = 0)


search = Button(root, text = "Submit", bg = 'red',fg = 'blue', command=submit)
search.grid(row = 3, column = 0)
label_1 = Label(root, text="Enter array elements separated by comma:")
label_1.grid(row=4, column=0)
#entry box in which we will enter arrays
entry = Entry(root)
entry.grid(row = 5, column = 0)
search_label = Label(root, text="Enter number to search:")
search_label.grid(row = 6, column = 0 )
#entry box where you enter number which you want to search
search_entry = Entry(root)
search_entry.grid(row = 7, column = 0)
search_button = Button(root, text="Search")
search_button.grid(row = 8, column = 0)
result_label = Label(root, text="")
result_label.grid(row = 9, column = 0)

root.mainloop()