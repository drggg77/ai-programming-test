import pandas as pd


def 정제(df):
    df = df.dropna(subset=["점수"]).copy()
    print(f"점수 결측 행 삭제 후: {len(df)}행")

    df = df.drop_duplicates().copy()
    print(f"중복 행 삭제 후: {len(df)}행")

    df["반"] = df["반"].str.strip()
    df["과목"] = df["과목"].str.strip()
    print(f"반·과목 공백 제거 후: {len(df)}행")

    df["점수"] = pd.to_numeric(df["점수"], errors="coerce")
    valid = df["점수"].between(0, 100) & (df["점수"] % 1 == 0)
    df = df.loc[valid].copy()
    df["점수"] = df["점수"].astype(int)
    print(f"점수 범위 및 정수 조건 적용 후: {len(df)}행")

    return df
df = pd.read_csv("scores_2026.csv")
df = 정제(df)

math_df = df.loc[df["과목"] == "수학"].copy()
print(len(math_df))

# 반별 점수 평균
반별_평균 = df.groupby("반")["점수"].mean()
print("반별 평균:\n", 반별_평균)

# 과목과 반별 점수 평균
과목_반별_평균 = df.groupby(["과목", "반"])["점수"].mean()
print("과목 및 반별 평균:\n", 과목_반별_평균)

# ③ 통계표 출력
통계표 = df.groupby("반").agg(
    개수=("점수", "count"),
    평균=("점수", "mean"),
    중앙값=("점수", "median"),
    최댓값=("점수", "max")
).round(2)

print("\n반별 통계표:\n", 통계표)

# STEP 4 pytest 검증용 함수
def 반별평균(df):
    return df.groupby("반")["점수"].mean().round(2).to_dict()