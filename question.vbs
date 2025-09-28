answer = MsgBox("Do you want to continue?", vbYesNo + vbQuestion, "Confirmation")
If answer = vbYes Then
    MsgBox "You chose Yes!", vbInformation, "Response"
Else
    MsgBox "You chose No!", vbExclamation, "Response"
End If