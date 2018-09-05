def get_rank(A, val, rank):
    print(A, val, rank)
    mid = len(A) // 2
    if len(A) == 1 and val >= A[0][0]:
        return A[0][1] + 1
    elif len(A) == 1 and val < A[0][0]:
        return rank
    if val >= A[mid][0]:
        rank = get_rank(A[:mid], val, A[mid][1] + 1)
    else:
        rank = get_rank(A[mid:], val, rank)
    return rank


def remove_duplicates(A):
    mem = set()
    for a in A:
        if a not in mem:
            mem.add(a)
            yield a


# Complete the climbingLeaderboard function below.
def _climbingLeaderboard(scores, alice):
    sorted_scores = list(remove_duplicates(scores))
    ranks = []
    sorted_scores = list(zip(sorted_scores, range(len(sorted_scores))))
    last_rank = len(sorted_scores)
    for alice_score in alice:
        rank = get_rank(sorted_scores[:last_rank], alice_score, 0)
        rank = rank if rank else len(sorted_scores) + 1
        last_rank = rank
        ranks.append(rank)
    return ranks

def climbingLeaderboard(scores, alice):
    results = []
    for x in alice:
        while len(scores) > 0 and scores[-1] <= x:
            del scores[-1]
        results.append(len(scores) + 1)
    return results


def climbingLeaderboard(scores, alice):
    sorted_scores = list(set(scores))
    sorted_scores.sort(reverse=True)
    ranks = []
    print(sorted_scores)
    for alice_score in alice:
        rank = 0
        for i_s, score in enumerate(sorted_scores):
            if alice_score >= score:
                rank = i_s + 1
                break
        ranks.append(rank if rank else len(sorted_scores)+1)
    return ranks


print(_climbingLeaderboard([100, 90, 90, 80, 75, 60], [50, 65, 77, 90, 102]))

scores = "295 294 291 287 287 285 285 284 283 279 277 274 274 271 270 268 268 268 264 260 259 258 257 255 252 250 244 241 240 237 236 236 231 227 227 227 226 225 224 223 216 212 200 197 196 194 193 189 188 187 183 182 178 177 173 171 169 165 143 140 137 135 133 130 130 130 128 127 122 120 116 114 113 109 106 103 99 92 85 81 69 68 63 63 63 61 57 51 47 46 38 30 28 25 22 15 14 12 6 4"
alice = "5 5 6 14 19 20 23 25 29 29 30 30 32 37 38 38 38 41 41 44 45 45 47 59 59 62 63 65 67 69 70 72 72 76 79 82 83 90 91 92 93 98 98 100 100 102 103 105 106 107 109 112 115 118 118 121 122 122 123 125 125 125 127 128 131 131 133 134 139 140 141 143 144 144 144 144 147 150 152 155 156 160 164 164 165 165 166 168 169 170 171 172 173 174 174 180 184 187 187 188 194 197 197 197 198 201 202 202 207 208 211 212 212 214 217 219 219 220 220 223 225 227 228 229 229 233 235 235 236 242 242 245 246 252 253 253 257 257 260 261 266 266 268 269 271 271 275 276 281 282 283 284 285 287 289 289 295 296 298 300 300 301 304 306 308 309 310 316 318 318 324 326 329 329 329 330 330 332 337 337 341 341 349 351 351 354 356 357 366 369 377 379 380 382 391 391 394 396 396 400"


scores = list(map(int, scores.split()))
alice = list(map(int, alice.split()))

print(_climbingLeaderboard(scores, alice))
