import json
import sys
from pathlib import Path

from cm_timer import cm_timer_1
from field import field
from gen_random import gen_random
from print_result import print_result
from unique import Unique


@print_result
def f1(data):
    return sorted(Unique(field(data, "job-name"), ignore_case=True), key=str.casefold)


@print_result
def f2(jobs):
    return list(filter(lambda job: job.casefold().startswith("программист"), jobs))


@print_result
def f3(jobs):
    return list(map(lambda job: f"{job} с опытом Python", jobs))


@print_result
def f4(jobs):
    salaries = gen_random(len(jobs), 100000, 200000)
    return [f"{job}, зарплата {salary} руб." for job, salary in zip(jobs, salaries)]


def main():
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).with_name("data_light.json")
    with path.open(encoding="utf-8") as file:
        data = json.load(file)

    with cm_timer_1():
        f4(f3(f2(f1(data))))


if __name__ == "__main__":
    main()
