' First popup: simple message
MsgBox "Yoooo it's 1x1x1x1", vbInformation, "Hi"

' Second popup: simple message
MsgBox "Why did you stop maining me :c", vbInformation, "Entanglement"

' third popup: question
answer = MsgBox("Can you main me again I wanna kill more survivors (especially Shedletsky) :p", vbYesNo + vbQuestion, "PLEASE MAIN ME AGAIN")

' Response based on answer
If answer = vbYes Then
    MsgBox "YAYYYYYYYYYYYY. Your my friend now :D", vbInformation, "hatred :>"
Else
    MsgBox "FEEL MY ENTANGLEMENT-", vbExclamation, "HATRED"
End If
