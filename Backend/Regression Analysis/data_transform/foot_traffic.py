import pandas as pd

# 데이터셋 불러오기
df_foot_traffic = pd.read_csv('C:/Users/SSAFY/Desktop/S10P22B206/Regression Analysis/data_set/길단위인구-상권.csv', encoding='cp949')

# 2021년 1분기부터 2023년 3분기까지의 데이터 추출
df_foot_traffic_2021 = df_foot_traffic[df_foot_traffic['year_code'] == 2021][['year_code', 'quarter_code', 'commercial_district_code', 'total_foot_traffic']]
df_foot_traffic_2022 = df_foot_traffic[df_foot_traffic['year_code'] == 2022][['year_code', 'quarter_code', 'commercial_district_code', 'total_foot_traffic']]
df_foot_traffic_2023 = df_foot_traffic[df_foot_traffic['year_code'] == 2023][['year_code', 'quarter_code', 'commercial_district_code', 'total_foot_traffic']]

df_foot_traffic_2023 = pd.merge(df_foot_traffic_2023, df_foot_traffic_2022, on=['quarter_code', 'commercial_district_code'], how='left', suffixes=('_now', '_previous'))
df_foot_traffic_2022 = pd.merge(df_foot_traffic_2022, df_foot_traffic_2021, on=['quarter_code', 'commercial_district_code'], how='left', suffixes=('_now', '_previous'))

df_foot_traffic = pd.concat([df_foot_traffic_2022, df_foot_traffic_2023])
df_foot_traffic['traffic_diff'] = df_foot_traffic['total_foot_traffic_now'] - df_foot_traffic['total_foot_traffic_previous']

# 컬럼명 변경
df_foot_traffic = df_foot_traffic.rename(columns={'year_code_now': 'year_code'})
df_foot_traffic.drop(columns=['year_code_previous'], inplace=True)

# # 결과 확인
print(df_foot_traffic)

# 새로운 CSV 파일 경로 지정
output_file_path = 'C:/Users/SSAFY/Desktop/S10P22B206/Regression Analysis/data_transform/길단위인구-상권.csv'

# 데이터프레임을 UTF-8 인코딩으로 CSV 파일로 저장
df_foot_traffic.to_csv(output_file_path, index=False, encoding='cp949')