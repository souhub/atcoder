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
            nは2以上の自然数である必要がある。それ以外を引数にした場合空のリストが返ってくる。
    """
    len_l = len(l)
    for i in range(len_l):
        for j in range(len_l-1-i):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    return l
