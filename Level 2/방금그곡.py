def solution(m, musicinfos):
    musicRename = {'C':'A', 'C#':'B', 'D':'C', 'D#':'D', 'E':'E','E#':'e', 'F':'F', 'F#':'G', 'G':'H', 'G#':'I', 'A':'j', 'A#':'k', 'B':'L','B#':'b'}
    musicinfos.reverse()
    answer = "(None)"
    mx = 0
    userMusic = ''
    while len(m) != 0:
        alpha = m[0]
        m = m[1:]
        if len(m) != 0 and m[0] == '#':
            alpha += '#'
            m = m[1:]
        userMusic += musicRename[alpha]
    for i in musicinfos:
        info = i.split(',')
        orgMusic = ""
        while len(info[3]) != 0:
            alpha = info[3][0]
            info[3] = info[3][1:]
            if len(info[3]) != 0 and info[3][0] == '#':
                alpha += '#'
                info[3] = info[3][1:]
            orgMusic += musicRename[alpha]
        time = 60*int(info[1][:2])+int(info[1][3:])-(60*int(info[0][:2])+int(info[0][3:]))
        music = orgMusic * (time // len(orgMusic)) + orgMusic[:time % len(orgMusic)]
        if userMusic in music and time >= mx:
            answer = info[2]
            mx = time
    return answer

"""
맞추긴 했지만 너무 더럽게 풀었다.
더 좋은 방법이 있었을텐데
"""