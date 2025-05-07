import time
import os
import sys
import random
import gmpy2
import multiprocessing
from math import log2, sqrt, log
from multiprocessing import Pool, cpu_count

os.system("cls||clear")
t = time.ctime()
sys.stdout.write(f"\033[?25l")
sys.stdout.write(f"\033[01;33m[+]\033[32m KANGAROO: \033[01;33m{t}\n")
sys.stdout.flush()

modulo = gmpy2.mpz(0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F)
Gx = gmpy2.mpz(0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798)
Gy = gmpy2.mpz(0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8)
PG = (Gx, Gy)

Z = (0, 0)  # zero-point, infinite in real x, y - plane

def add(P, Q, p=modulo):
    Px, Py = P
    Qx, Qy = Q
    if P == Z:
        return Q
    elif Q == Z:
        return P
    elif Px == Qx and (Py != Qy or Py == 0):
        return Z
    elif Px == Qx:
        m = (3 * Px * Px) * gmpy2.invert(2 * Py, p) % p
    else:
        m = (Qy - Py) * gmpy2.invert(Qx - Px, p) % p
   
    x = (m * m - Px - Qx) % p
    y = (m * (Px - x) - Py) % p
    return (x, y)


def mul2(P, p=modulo):
    Px, Py = P
    if P == Z:
        return Z
    m = gmpy2.f_mod(3 * Px * Px * gmpy2.invert(2 * Py, p), p)
    x = gmpy2.f_mod(m * m - 2 * Px, p)
    y = gmpy2.f_mod(m * (Px - x) - Py, p)
    return (x, y)

def mulk(k, P=PG, p=modulo):
    if k == 0:
        return Z
    elif k == 1:
        return P
    elif k % 2 == 0:
        return mulk(k // 2, mul2(P, p), p)
    else:
        return add(P, mulk((k - 1) // 2, mul2(P, p), p), p)

def X2Y(X, y_parity, p=modulo):
    X_cubed = gmpy2.powmod(X, 3, p)
    X_squared = gmpy2.powmod(X, 2, p)
    tmp = gmpy2.f_mod(X_cubed + 7, p)
    Y = gmpy2.powmod(tmp, gmpy2.f_div(gmpy2.add(p, 1), 4), p)
    if y_parity == 1:
        Y = gmpy2.f_mod(-Y, p)
    return Y

def comparator(A, Ak, B, Bk, core_number, random_seed):
    result = set(A).intersection(set(B))
    if result:
        sol_kt = A.index(next(iter(result)))
        sol_kw = B.index(next(iter(result)))
        HEX = "%064x" % abs(Ak[sol_kt] - Bk[sol_kw])
        dec = int(HEX, 16)
        total_time = time.time() - starttime
        print('\n[+] total time: %.2f sec' % (total_time))
        t = time.ctime()
        print(f"\033[32m[+] PUZZLE SOLVED: {t}, Core: {core_number+1:02} \033[0m")
        print(f"\033[32m[+] Random seed used: {random_seed} \033[0m")
        print(f"\033[32m[+] Private key (dec) : {dec} \033[0m")
        dash_line = '-' * 140
        with open("KEYFOUNDKEYFOUND.txt", "a") as file:
            file.write(f"\n{dash_line}")
            file.write("\n\nSOLVED " + t)
            file.write(f"\nTotal Time: {total_time:.2f} sec")
            file.write(f"\nCore: {core_number+1:02}")
            file.write(f"\nRandom seed: {random_seed}")
            file.write("\nPrivate Key (decimal): " + str(dec))
            file.write("\nPrivate Key (hex): " + HEX)
            file.write(f"\n{dash_line}")
        file.close()
        return True
    else:
        return False

def check(P, Pindex, DP_rarity, A, Ak, B, Bk, core_number, random_seed):
    modulo_val = P[0] % DP_rarity
    if modulo_val == 0:
        A.append(gmpy2.mpz(P[0]))
        Ak.append(gmpy2.mpz(Pindex))
        return comparator(A, Ak, B, Bk, core_number, random_seed)
    else:
        return False

def generate_powers_of_two(hop_modulo):
    return [gmpy2.mpz(1 << pw) for pw in range(hop_modulo)]

def search(thread_id, P, W0, DP_rarity, Nw, Nt, hop_modulo, upper_range_limit, lower_range_limit, result_queue, powers_of_two):
    pid = os.getpid()
    core_number = pid % cpu_count()
    #Random seed Config
    #constant_prefix = b''  #back to no constant
    constant_prefix = b''
    prefix_length = len(constant_prefix)
    length = 8    #change to 20 for puzzle 135
    ending_length = length - prefix_length
    ending_bytes = os.urandom(ending_length)
    random_seed = constant_prefix + ending_bytes
    random.seed(random_seed)
    print(f"[+] [Core]: {core_number+1:02}, [Random seed]: {random_seed}")   
    t = [gmpy2.mpz(lower_range_limit + gmpy2.mpz(random.randint(0, upper_range_limit - lower_range_limit))) for _ in range(Nt)]
    T = [mulk(ti) for ti in t]
    dt = [gmpy2.mpz(0) for _ in range(Nt)]
   
    w = [gmpy2.mpz(random.randint(0, upper_range_limit - lower_range_limit)) for _ in range(Nw)]
    W = [add(W0, mulk(wk)) for wk in w]
    dw = [gmpy2.mpz(0) for _ in range(Nw)]
   
    Hops, Hops_old = 0, 0
    t0 = time.time() 
    memo = {}
    solution_found = False
   
    while not solution_found:
        for k in range(Nt):
            Hops += 1
            pw = T[k][0] % hop_modulo
            if pw not in memo:
                memo[pw] = powers_of_two[pw]
            dt[k] = memo[pw]
            if check(T[k], t[k], DP_rarity, T, t, W, w, core_number, random_seed):
                result_queue.put((thread_id, T[k], t[k], W[k], w[k], core_number, random_seed))
                solution_found = True
                break
            t[k] += dt[k]
            T[k] = add(P[int(pw)], T[k])
        if solution_found:
            break
           
        for k in range(Nw):
            Hops += 1
            pw = W[k][0] % hop_modulo
            if pw not in memo:
                memo[pw] = powers_of_two[pw]
            dw[k] = memo[pw]
            if check(W[k], w[k], DP_rarity, W, w, T, t, core_number, random_seed):
                result_queue.put((thread_id, T[k], t[k], W[k], w[k], core_number, random_seed))
                solution_found = True
                break
            w[k] += dw[k]
            W[k] = add(P[int(pw)], W[k])
        if solution_found:
            break
           
        t1 = time.time()
        elapsed_time = t1 - starttime
        if t1 - t0 > 1 and thread_id == 0:
            hops_per_second = (Hops - Hops_old) / (t1 - t0) * cores
            hours, rem = divmod(elapsed_time, 3600)
            minutes, seconds = divmod(rem, 60)
            elapsed_time_str = f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}"
            p_2 = f'{log2(Hops*cores):.2f}'
            print(f'[+] [Hops: 2^{p_2} <-> {hops_per_second:.0f} h/s] [{elapsed_time_str}]', end='\r', flush=True)
            t0 = t1
            Hops_old = Hops
   
    print('\r[+] Hops:', Hops* cores)
    print('[+] Average time to solve: %.2f sec' % ((time.time()-starttime)))

def main():
    result_queue = multiprocessing.Queue()
    processes = [
        multiprocessing.Process(target=search, args=(i, P, W0, DP_rarity, Nw, Nt, hop_modulo, upper_range_limit, lower_range_limit, result_queue, powers_of_two)) for i in range(cores)
    ]
    for p in processes:
        p.start()
   
    # Wait for a result
    result = result_queue.get()
    thread_id, T_k, t_k, W_k, w_k, core_number, random_seed = result
   
    # Print the successful core and seed
    print(f"\n[+] Solution found by Core: {core_number+1:02}")
    print(f"[+] Random seed used: {random_seed}")
   
    # Terminate all processes
    for p in processes:
        p.terminate()

# Configuration for the puzzle
cores = cpu_count()
puzzle = 40
compressed_public_key = "03a2efa402fd5268400c77c20e574ba86409ededee7c4020e4b9f0edbee53de0d4"
kangaroo_power = 3 
lower_range_limit = 2 ** (puzzle - 1)
upper_range_limit = (2**puzzle) - 1

DP_rarity = 1 << int(((puzzle -  2*kangaroo_power)/2 - 2))
hop_modulo = ((puzzle - 1) // 2) + kangaroo_power
Nt = Nw = 2**kangaroo_power

# Precompute powers of two for faster access
powers_of_two = generate_powers_of_two(hop_modulo)

(T, t, dt), (W, w, dw), (A, Ak, B, Bk) = ([], [], []), ([], [], []), ([], [], [], [])
print('[+] [Tame and Wild herds are prepared]')

if len(compressed_public_key) == 66:
    X = gmpy2.mpz(compressed_public_key[2:66], 16)
    Y = X2Y(X, gmpy2.mpz(compressed_public_key[:2]) - 2)
else:
    print("[error] pubkey len(66/130) invalid!")

W0 = (X,Y)
starttime = oldtime = time.time()

Hops = 0

P = [PG]
for k in range(255):
    P.append(mul2(P[k])) 
print('[+] [P-table prepared]')

print(f"[+] [Puzzle: {puzzle}]")
print(f"[+] [Lower range limit: {lower_range_limit}]")
print(f"[+] [Upper range limit: {upper_range_limit}]")
print(f"[+] [Expected Hops: 2^{log2(2.2 * sqrt(1 << (puzzle-1))):.2f} ({int(2.2 * sqrt(1 << (puzzle-1)))})]")
print(f"[+] [Using {cores} CPU cores for parallel search]")

if __name__ == '__main__':
    main()
