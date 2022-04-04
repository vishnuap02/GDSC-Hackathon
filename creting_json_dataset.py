list="Students \n { \n "
list+="[ \n "

first_names = []
last_names = ['Parvatikar','Reddy', 'Patel', 'Sharma', 'Tyagi', 'Singh', 'Verma', 'Agarwal']
names = "Vishnu Amanda2. Jay3. Anna4. Abdullah5. Tamara6. Abdul7. Maya8. Jai9. Tara10. Rohan11. Ana12. Ajay13. Aisha14. Ram15. Alisha16. Sanjay17. Anya18. Ravi19. Lila20. Arman21. Amara22. Amit23. Fatima24. Sandeep25. Anika26. Vijay27. Anita28. Rahul29. Trisha30. Ira31. Arya32. Ibrahim33. Anjali34. Ashwin35. Jasmin36. Kiran37. Priya38. Krish39. Asha40. Arjun41. Ida42. Rajesh43. Riya44. Dev45. Mira46. Deepak47. Shyla48. Arun49. Mara50. Anand"
name = ''.join([i for i in names if not i.isdigit()])
name = ''.join([i for i in name if not i == '.'])
first_names = name.split(' ')
age = [i for i in range(18, 35)]

for i in range(1,130):

    strn = "cs20b" + str(1000+i)
    fno=i%4
    names = first_names[i%50]+" "+last_names[i%7]
    list+="{ \n "+'"id":'+'"{}"'.format(strn) + ', \n' + '"Name":'+'"{}"'.format(names) +', \n'+'"floor":'+'"{}"'.format(fno) + '\n },\n'


list+=" \n ] \n } "
print(list)
