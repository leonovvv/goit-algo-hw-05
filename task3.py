import timeit
import random

# Реалізація алгоритму Боєра-Мура
def boyer_moore_search(text, pattern):
    m, n = len(pattern), len(text)
    if m == 0:
        return 0
    skip = {}
    for i in range(m - 1):
        skip[pattern[i]] = m - i - 1
    i = m - 1
    while i < n:
        j = m - 1
        while text[i] == pattern[j]:
            if j == 0:
                return i
            i -= 1
            j -= 1
        i += skip.get(text[i], m)
    return -1

# Реалізація алгоритму Кнута-Морріса-Пратта
def kmp_search(text, pattern):
    def compute_lps(pattern):
        m = len(pattern)
        lps = [0] * m
        length = 0
        i = 1
        while i < m:
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    n, m = len(text), len(pattern)
    lps = compute_lps(pattern)
    i = j = 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == m:
            return i - j
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1

# Реалізація алгоритму Рабіна-Карпа
def rabin_karp_search(text, pattern, d=256, q=101):
    n, m = len(text), len(pattern)
    if m == 0 or m > n:
        return -1
    h = pow(d, m-1) % q
    p = t = 0
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q
    for i in range(n - m + 1):
        if p == t:
            if text[i:i + m] == pattern:
                return i
        if i < n - m:
            t = (t - ord(text[i]) * h) * d + ord(text[i + m])
            t %= q
    return -1

def get_sample(text, size):
    rand = random.randint(0, len(text1)-size)
    return text[rand: rand+10]


# Читаємо текстові файли
with open('article1.txt', 'r', encoding='cp1251') as file1, open('article2.txt', 'r', encoding='utf-8-sig') as file2:
    text1 = file1.read()
    text2 = file2.read()

# Вибираємо підрядки для пошуку
existing_substring1 = get_sample(text1,10)
existing_substring2 = get_sample(text2,10)
non_existing_substring = "thisdoesnotexistinthetext"

# Функція для замірів часу
def measure_search_time(search_function, text, pattern):
    return timeit.timeit(lambda: search_function(text, pattern), number=1000)

# Вимірюємо час виконання для кожного алгоритму та підрядка
print("Article 1 - Existing Substring")
print(f"Boyer-Moore: {measure_search_time(boyer_moore_search, text1, existing_substring1):.5f} seconds")
print(f"KMP: {measure_search_time(kmp_search, text1, existing_substring1):.5f} seconds")
print(f"Rabin-Karp: {measure_search_time(rabin_karp_search, text1, existing_substring1):.5f} seconds")

print("\nArticle 1 - Non-existing Substring")
print(f"Boyer-Moore: {measure_search_time(boyer_moore_search, text1, non_existing_substring):.5f} seconds")
print(f"KMP: {measure_search_time(kmp_search, text1, non_existing_substring):.5f} seconds")
print(f"Rabin-Karp: {measure_search_time(rabin_karp_search, text1, non_existing_substring):.5f} seconds")

print("\nArticle 2 - Existing Substring")
print(f"Boyer-Moore: {measure_search_time(boyer_moore_search, text2, existing_substring2):.5f} seconds")
print(f"KMP: {measure_search_time(kmp_search, text2, existing_substring2):.5f} seconds")
print(f"Rabin-Karp: {measure_search_time(rabin_karp_search, text2, existing_substring2):.5f} seconds")

print("\nArticle 2 - Non-existing Substring")
print(f"Boyer-Moore: {measure_search_time(boyer_moore_search, text2, non_existing_substring):.5f} seconds")
print(f"KMP: {measure_search_time(kmp_search, text2, non_existing_substring):.5f} seconds")
print(f"Rabin-Karp: {measure_search_time(rabin_karp_search, text2, non_existing_substring):.5f} seconds")
