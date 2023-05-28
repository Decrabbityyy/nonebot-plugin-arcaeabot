


def calculate_rating(defnum: float, score: int) -> float:
        '''计算rating，谱面定数小于等于0视为Unrank，返回值会为-1，这里的defnum = Chart const'''
        if not defnum or defnum <= 0:
            # 谱面没定数或者定数小于等于0被视作Unrank
            return -1

        if score >= 10000000:
            ptt = defnum + 2
        elif score < 9800000:
            ptt = defnum + (score-9500000) / 300000
            ptt = max(ptt, 0)
        else:
            ptt = defnum + 1 + (score-9800000) / 200000

        return ptt