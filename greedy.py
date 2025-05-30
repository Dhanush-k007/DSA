def read(n, book, target):
    book.sort()  # Sort the array
    left = 0
    right = n - 1

    while left < right:
        total = book[left] + book[right]
        if total == target:
            return "YES"
        elif total < target:
            left += 1
        else:
            right -= 1

    return "NO"
