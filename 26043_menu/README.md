# 식당 메뉴
## 문제
여러 명의 학생이 식사하기 위하여 학교 식당을 향해 달려가고 있다. 학교 식당에 도착한 학생은 식당 입구에 줄을 서서 대기한다. 학교 식당에 먼저 도착한 학생이 나중에 도착한 학생보다 식당 입구의 앞쪽에서 대기한다. 식사는 1인분씩 준비된다. 식사 1인분이 준비되면 식당 입구의 맨 앞에서 대기 중인 학생 1명이 식당으로 들어가서 식사를 시작한다. 식사를 시작한 학생은 항상 식사를 마친다.

학교 식당에서는 두 가지 메뉴가 제공되고 각각의 학생은 두 가지 메뉴 중에서 본인이 좋아하는 메뉴를 결정한 상태다. 학생이 학교 식당에 도착하고 식사가 준비되는 n개의 정보가 저장된 S가 주어진다. S에 저장된 첫 번째 정보부터 n번째 정보까지 순서대로 처리한 경우, 본인이 좋아하는 메뉴를 먹은 학생 목록 A와 본인이 좋아하지 않는 메뉴를 먹은 학생 목록 B와 학교 식당에 도착하였으나 식사를 하지 못한 학생 목록 C를 출력하자.

S에 저장된 n개의 식당 정보는 아래 두 가지 유형으로 구분된다. 첫 번째가 유형 1, 두 번째가 유형 2다.

1 a b: 학생 번호가 양의 정수 a이고 좋아하는 메뉴 번호가 양의 정수 b인 학생 1명이 학교 식당에 도착하여 식당 입구의 맨 뒤에 줄을 서기 시작한다.
2 b: 메뉴 번호가 양의 정수 b인 식사 1인분이 준비되어 식당 입구의 맨 앞에서 대기 중인 학생 1명이 식사를 시작한다.
식사 1인분이 준비될 때는 식당 입구에서 대기 중인 학생이 항상 존재한다. 식당 입구에 줄을 서서 대기하였으나 식사가 준비 안 된 학생은 식사를 못 한다.

## 입력
첫 번째 줄에 n이 주어진다.

두 번째 줄부터 n개의 줄에 걸쳐 한 줄에 하나의 정보가 주어진다. 각 정보는 유형 1, 2중 하나이다.

## 출력
첫 번째 줄에 학생 목록 A에 있는 학생 번호를 빈칸을 사이에 두고 오름차순으로 출력한다.

두 번째 줄에 학생 목록 B에 있는 학생 번호를 빈칸을 사이에 두고 오름차순으로 출력한다.

세 번째 줄에 학생 목록 C에 있는 학생 번호를 빈칸을 사이에 두고 오름차순으로 출력한다.

학생 목록에 학생이 없는 경우 학생 번호 대신 None을 출력한다.