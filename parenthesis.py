




def parenthesis(n,temp,opened_parenthesis, closed_parenthesis, all_parenthesis_list):
  # CONSIDER CLOSING IF NO OPENED PARENTHESID AND CLOSED PARENTHESIS = N 
  if closed_parenthesis == n and opened_parenthesis == 0:
    all_parenthesis_list.append(temp)
    return
  else:
    if opened_parenthesis+closed_parenthesis<n:
      # CONSIDER OPENING A NEW PARENTHESIS 
      parenthesis(n,temp+"(",opened_parenthesis+1,closed_parenthesis,all_parenthesis_list)

    # CONSIDER CLOSING PARENTHESIS 
    if opened_parenthesis!=0:
      parenthesis(n,temp+")", opened_parenthesis-1,closed_parenthesis+1,all_parenthesis_list)

def p(n):
  all_combos=[]
  parenthesis(n,"",0,0,all_combos)
  return all_combos



res=p(3)
print(res)