def cal_freq(text):
    text = text.upper()
    freq = {}
    total = 0

    for char in text:
        if char.isalpha():
            freq[char] = freq.get(char, 0) + 1
            total += 1
            
    print("Alphabet Frequency:")
    for alphabet, cnt in sorted(freq.items()):
        freq = "{:.2f}".format((cnt/total)*100)
        print(f"{alphabet}: {freq}%")

text = 'C UYGHARMZ IUWMPRWIR GAIR YVRMP MBHMZWMPUM C VMMXWPE YV PYR VCZ ZMGYQMD VZYG CXCZG YP CPCXKTWPE CPD MBHXYZM RNM VXYYD YV CDQCPUMD OPYSXMDEM SNWUN MCUN KMCZ LZWPEI SWRN WR'
cal_freq(text)