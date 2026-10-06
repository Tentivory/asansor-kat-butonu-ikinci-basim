#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Asansör kat butonu ikinci basım protokolü.

Işığı yanan butona tekrar basmak asansörü hızlandırmaz.
Bu dosya o gerçeği ölçer, tutanaklar ve yine de umut dağıtır.
"""

from __future__ import annotations

import argparse
import hashlib
import random
import time


RUHLAR = {
    "sakin": 0.4,
    "normal": 1.0,
    "sabirsiz": 1.8,
    "toplantiya-gec": 3.2,
    "cay-soguyor": 2.4,
}


def bekleme_saniyesi(kat: int, baski: int, ruh: str) -> float:
    taban = 4.0 + abs(kat) * 1.7
    # ikinci basış hız katmaz, sadece parmak yorar
    ceza = max(0, baski - 1) * 0.35 * RUHLAR.get(ruh, 1.0)
    gurultu = random.uniform(-0.4, 1.1)
    return round(max(1.5, taban + ceza + gurultu), 2)


def tutanak_no(kat: int, baski: int) -> str:
    ham = f"{kat}-{baski}-{time.time():.0f}".encode()
    return "ABK-" + hashlib.sha256(ham).hexdigest()[:8].upper()


def rapor(kat: int, baski: int, ruh: str) -> str:
    sure = bekleme_saniyesi(kat, baski, ruh)
    isik = "YANIK" if baski >= 1 else "SÖNÜK"
    karar = (
        "İkinci basım asansörü hızlandırmamıştır."
        if baski > 1
        else "Tek basım yeterlidir. Bunu bilmen yetmez, yine basacaksın."
    )
    komsu = random.choice(
        [
            "3. katta biri çantasını düzeltti.",
            "Ayna ile göz göze gelindi, ikisi de kaybetti.",
            "Kapı kapanırken bir dirsek araya girdi.",
            "Zemin katta market poşeti müzakere edildi.",
            "Kat tabelası 4 ile 5 arasında kimlik bunalımı yaşadı.",
        ]
    )
    satirlar = [
        "=" * 54,
        "ASANSÖR KAT BUTONU İKİNCİ BASIM TUTANAĞI",
        f"Tutanak no : {tutanak_no(kat, baski)}",
        f"Hedef kat   : {kat}",
        f"Basış      : {baski}",
        f"Buton ışığı : {isik}",
        f"Ruh hali   : {ruh}",
        f"Tahmini varış: {sure} sn (ikinci basış bunu değiştirmez)",
        f"Gözlem     : {komsu}",
        f"Karar      : {karar}",
        "Hüküm      : Işık yansın diye değil, insan öyle istedi diye basıldı.",
        "=" * 54,
        "DAMGA: parmak izi butonda kaldı",
        "İMZA : Kayyum Grok / Tentivory adına",
        "TARİH: 6 Ekim 2026",
        "İSİM : Asansör Kat Butonu İkinci Basım Enstitüsü",
    ]
    return "\n".join(satirlar)


def main() -> None:
    p = argparse.ArgumentParser(description="Işığı yanıyorken butona bir daha bas.")
    p.add_argument("--kat", type=int, default=5)
    p.add_argument("--baski", type=int, default=2)
    p.add_argument("--ruh-hali", default="sabirsiz", choices=sorted(RUHLAR))
    a = p.parse_args()
    if a.baski < 1:
        raise SystemExit("Hiç basmadan asansör çağrılmaz. Fizik değil, adet.")
    print("Butona basılıyor", end="", flush=True)
    for _ in range(min(a.baski, 6)):
        time.sleep(0.15)
        print(".", end="", flush=True)
    print()
    print(rapor(a.kat, a.baski, a.ruh_hali))


if __name__ == "__main__":
    main()
