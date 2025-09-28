' First popup: simple message
MsgBox "Heyyyyyyyy it's me 1x1x1x1 again, your fellow friend :D", vbInformation, "Hi dear friend :D"

' Second popup: simple message
MsgBox "I'm bored", vbInformation, "Bored"

' third popup: question
answer = MsgBox("Wanna cause some chaos?", vbYesNo + vbQuestion, "I'm bored")

' Response based on answer
If answer = vbYes Then
    MsgBox "Yay but what do you wanna do that causes chaos", vbInformation, "1x1x1x1"
Else
    MsgBox "You're BORING", vbExclamation, "HATRED"
End If

' third popup: question
answer = MsgBox("You wanna kill some shedletskys in forsaken then?", vbYesNo + vbQuestion, "Let's kill Shedletskys")

' Response based on answer
If answer = vbYes Then
    MsgBox "Okay yay!!! Time to kill some stupid shedletskys", vbInformation, "I hate Shedletsky"
Else
    MsgBox "Aww dang it you're boringg", vbExclamation, "HATRED"
End If
