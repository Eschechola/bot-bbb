import webbrowser
import pyautogui
import time

def moveAndClick(eiX, eiY, moveSleep = 0, clickSleep = 0):
    time.sleep(moveSleep)
    pyautogui.moveTo(eiX, eiY)

    time.sleep(clickSleep)
    pyautogui.click()


def voteFirst(urlBBB):
    print("Votar no primeiro participante do paredão!")

def voteSecond(urlBBB):
    print("Votar no segundo participante do paredão!")

def voteThird(urlBBB):
    print("Votar no terceito participante do paredão!")
    
    webbrowser.open(urlBBB)
    
    votes = 0

    while(1):
        #Move and click in the person icon
        moveAndClick(925, 850, 1, 1)

        #Move and click in the captcha box
        moveAndClick(840, 1010, 1, 0.3)

        #Move to vote again
        moveAndClick(1107, 459, 13, 0.3)

        votes +=1
        print("Foram efetuados "+ str(votes) +" votos no terceiro participante!")

#https://gshow.globo.com/realities/bbb/bbb21/votacao/paredao-bbb21-vote-para-eliminar-arthur-gilberto-ou-karol-conka-838ec4d5-7d17-4263-a335-29e13c3a769b.ghtml

print("\n!!!!! AVISO !!!!!")
print("Bot funcional somente na resolução full hd! (1920x1080)")
print("Aperte ENTER para prosseguir.")
command = input()

urlBBB = input("Url de votação no BBB: ")

while(1):
    participantToVote = int(input("Digite o número do participante que deseja votar: "))
        
    if participantToVote == 1:
        voteFirst(urlBBB)
        break

    elif participantToVote == 2:
        voteSecond(urlBBB)
        break

    elif participantToVote == 3:
        voteThird(urlBBB)
        break

    else:
        print("\n\nOpção inválida! Escolha entre 1, 2 e 3\n\n")
        break





