def trial_division(n: int) -> list[int]:
    """trial_division
        素因数分解を行う関数

        Args:
            n (int): 素因数分解の対象とする自然数を入力。

        Returns:
            list[int]: 素因数分解の結果を返す。

        Examples:
            >>> trial_division(72)
                return [2, 2, 2, 3, 3]

        Note:
            nは2以上の自然数である必要がある。それ以外を引数にした場合空のリストが返ってくる。
    """
    ans = []
    f = 2  # The first possible factor.
    while n > 1:
        if n % f == 0:
            ans.append(f)
            n /= f
        else:
            f += 1
    return ans


def bubble_sort(l: list) -> list:
    """bubble_sort
        Bubble sort を行う関数

        Args:
            l (list): 昇順にソートしたいリストを入力。

        Returns:
            (1) list[int]: 配列が数列の場合、昇順にソートされたものを返す。
            (2) list[str]: 配列が文字列の場合、名前の順にソートされたものを返す。

        Examples:
            >>> (1) lにlist[int]を渡した場合。
                    bubble_sort([1,5,2,6,0,1,-2,-3])
                    return [-3, -3, 0, 1, 1, 2, 5, 6]
                (2) lにlist[str]を渡した場合。
                    bubble_sort('banana, 'apple', 'grape', 'tomato')
                    return ['apple', 'banana', 'grape', 'tomato']

        Note:
            int型、str型のどちらも対応可能。
    """
    len_l = len(l)
    for i in range(len_l):
        for j in range(len_l-1-i):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    return l


def coocktail_sort(l: list) -> list:
    """coocktail_sort
        Coocktail sort を行う関数

        Args:
            l (list): 昇順にソートしたいリストを入力。

        Returns:
            (1) list[int]: 配列が数列の場合、昇順にソートされたものを返す。
            (2) list[str]: 配列が文字列の場合、名前の順にソートされたものを返す。

        Examples:
            >>> (1) lにlist[int]を渡した場合。
                    bubble_sort([1,5,2,6,0,1,-2,-3])
                    return [-3, -3, 0, 1, 1, 2, 5, 6]
                (2) lにlist[str]を渡した場合。
                    bubble_sort('banana, 'apple', 'grape', 'tomato')
                    return ['apple', 'banana', 'grape', 'tomato']

        Note:
            int型、str型のどちらも対応可能。
    """
    len_l = len(l)
    start = 0
    end = len_l-1
    swapped = True
    while swapped:
        swapped = False
        for i in range(start, end):
            if l[i] > l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]
                swapped = True

        if not swapped:
            break

        end = end-1

        for j in range(end-1, start-1, -1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
                swapped = True

        start = start+1

    return l


def selection_sort(l: list) -> list:
    """coocktail_sort
        Selection sort を行う関数

        Args:
            l (list): 昇順にソートしたいリストを入力。

        Returns:
            (1) list[int]: 配列が数列の場合、昇順にソートされたものを返す。
            (2) list[str]: 配列が文字列の場合、名前の順にソートされたものを返す。

        Examples:
            >>> (1) lにlist[int]を渡した場合。
                    bubble_sort([1,5,2,6,0,1,-2,-3])
                    return [-3, -3, 0, 1, 1, 2, 5, 6]
                (2) lにlist[str]を渡した場合。
                    bubble_sort('banana, 'apple', 'grape', 'tomato')
                    return ['apple', 'banana', 'grape', 'tomato']

        Note:
            int型、str型のどちらも対応可能。
    """
    len_l = len(l)
    for i in range(len_l):
        min_idx = i
        for j in range(i+1, len_l):
            if l[min_idx] > l[j]:
                min_idx = j
        l[i], l[min_idx] = l[min_idx], l[i]

    return l


def insertion_sort(l: list) -> list:
    """coocktail_sort
        Insertion sort を行う関数

        Args:
            l (list): 昇順にソートしたいリストを入力。

        Returns:
            (1) list[int]: 配列が数列の場合、昇順にソートされたものを返す。
            (2) list[str]: 配列が文字列の場合、名前の順にソートされたものを返す。

        Examples:
            >>> (1) lにlist[int]を渡した場合。
                    bubble_sort([1,5,2,6,0,1,-2,-3])
                    return [-3, -3, 0, 1, 1, 2, 5, 6]
                (2) lにlist[str]を渡した場合。
                    bubble_sort('banana, 'apple', 'grape', 'tomato')
                    return ['apple', 'banana', 'grape', 'tomato']

        Note:
            int型、str型のどちらも対応可能。
    """
    len_l = len(l)
    for i in range(1, len_l):
        temp = l[i]
        j = i-1

        while j >= 0 and l[j] > temp:
            l[j+1] = l[j]
            j -= 1

        l[j+1] = temp

    return l


if __name__ == '__main__':
    l = [2, 7, 5, 25, 86, 4, 2, 22, 56, 4]
    print(insertion_sort(l))
