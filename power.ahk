;
; AutoHotkey Version: 1.x
; Language:       English
; Platform:       Win9x/NT
; Author:         viren <viren@outlook.com>
;

#NoEnv
SendMode Input
SetWorkingDir %A_ScriptDir%
#NoTrayIcon

; turn off screen
#z::
    SendMessage 0x112, 0xF170, 2, , Program Manager
    Return
    
; sleep
#s::
    DllCall("PowrProf\SetSuspendState", "int", 0, "int", 0, "int", 0)
    Return
    
; hibernate
;#h::    
    ;DllCall("PowrProf\SetSuspendState", "int", 1, "int", 0, "int", 0)
    ;Return
