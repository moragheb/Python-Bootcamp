def BlackJack_newround():
    global carddeck
    quit=False
    if len(carddeck)<=4 :
        carddeck=Deck()
    player1.reset()
    dealer.reset()
    player1.Currenthand.addtohand(carddeck.drawcard())
    player1.printhand()
    dealer.Currenthand.addtohand(carddeck.drawcard())
    dealer.printhand()
    while player1.bet()==False:
        choice=int(input(player1.Name +" do you want to 1-deposit money or 2-quit "))
        if choice in [1,2]:
            if choice ==1 :
                player1.deposit()
                pass
            else:
                printmd(dealer.Name+"  wins "+ player1.Name+" is a loser")
                dealer.WinsRecord+=1
                player1.Betsize=0
                return False
                break
    if player1.Betsize==-1:
        printmd(dealer.Name+"  wins "+ player1.Name+" is a loser")
        dealer.WinsRecord+=1
        player1.Betsize=0
        return False
        
    while player1.Bust() ==2:
            if len(player1.Currenthand)==1:
                   player1.Currenthand.addtohand(carddeck.drawcard())
                   player1.printhand()
                   dealer.Currenthand.addtohand(carddeck.drawcard())
                   dealer.printhand()
                   if player1.Bust()==0:
                         printmd(dealer.Name+"  wins "+ player1.Name+" Busted Balance is : " str(player1.Balance))
                         dealer.WinsRecord+=1
                         return True
                   elif player1.Bust()==1:
                         player1.WinsRecord+=1
                         player1.Balance+=player1.Betsize*2
                         printmd(player1.Name+"  wins Balance is : "+ str(player1.Balance))
                         return True
                   elif dealer.Bust() ==0:
                         
                         player1.WinsRecord+=1
                         player1.Balance+=player1.Betsize*2
                         printmd(Player1.Name+"  wins "+ dealer.Name+" Busted Balnce is "+ str(player1.Balance))
                         return True
                   elif dealer.Bust()==1:
                         printmd(player1.Name+"  wins Balnce is"+str(player1.Balance))
                         dealer.WinsRecord+=1
                         return True
            else :
                while True:
                     hitorstay=input(player1.Name +"press a for hit press b for stay or q for Quit")
                     if(hitorstay in["a","b","q"]):
                            break
                if hitorstay=="a":
                    
                     while player1.bet()==False:
                         choice=int(input(player1.Name +" do you want to 1-deposit money or 2-quit "))
                         if choice in [1,2]:
                              if choice ==1 :
                                    player1.deposit()
                                    pass
                              else:

                                    dealer.WinsRecord+=1
                                    printmd(dealer.Name+"  wins "+ player1.Name+" is a loser  Balance is :"+str(player1.Balance))
                                    return False
                     if player1.Betsize==-1:
                          printmd(dealer.Name+"  wins "+ player1.Name+" is a loser")
                          dealer.WinsRecord+=1
                          player1.Betsize=0
                          return False
                     player1.Currenthand.addtohand(carddeck.drawcard())
                     player1.printhand()
                     dealer.Currenthand.addtohand(carddeck.drawcard())
                     dealer.printhand()
                     if player1.Bust()==0:
                             dealer.WinsRecord+=1
                             player1.Betsize=0
                             printmd(dealer.Name+"  wins "+ player1.Name+" Busted Balance is : " str(player1.Balance))
               
                             return True
                     elif player1.Bust()==1:
                             player1.WinsRecord+=1
                             player1.Balance+=player1.Betsize*2
                             printmd(player1.Name+"  wins Balance is : "+ str(player1.Balance))
                             player1.Betsize=0
                             printmd(dealer.Name+"  wins "+player1.Name+"  Balance is "+str(player1.Balance))
                             return True
                     elif dealer.Bust() ==0:
                             player1.WinsRecord+=1
                             player1.Balance+=player1.Betsize*2
                             printmd(player1.Name+"  wins "+ dealer.Name+" Busted Balance is "+ str(player1.Balance))
                             return True
                     elif dealer.Bust()==1:
                             printmd(dealer.Name+"  wins "+player1.Name+"  Balance is "+str(player1.Balance))
                             dealer.WinsRecord+=1
                             return True
                     else:
                        pass
                if hitorstay=="b":
                     if player1.Currenthand.sumofhand()>dealer.Currenthand.sumofhand():
                            
                             player1.WinsRecord+=1
                             player1.Balance+=player1.Betsize*2
                             printmd(player1.Name+"  wins Balance is : "+ str(player1.Balance))
                             return True
                     else:
                             printmd(dealer.Name+"  wins"+player1.Name+"  balance is "+str(player1.Balance))
                             dealer.WinsRecord+=1
                             return True
                else:
                     return False

        

                                     
                                        
             
                    
  
                    