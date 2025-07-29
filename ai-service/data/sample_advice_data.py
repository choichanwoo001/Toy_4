"""
초기 조언 데이터베이스를 위한 샘플 데이터
다양한 상황과 감정에 대한 조언들을 포함
ChromaDB 호환성을 위해 메타데이터는 문자열 형태로 저장
"""

SAMPLE_ADVICE_DATA = [
  {
    "content":"오늘 아침 따뜻한 햇살을 받으며 산책하니 마음이 평온해졌어요.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"가족과 함께 보낸 주말 시간이 정말 소중하고 행복했습니다.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"좋아하는 음악을 들으며 집안일을 하니 기분이 상쾌해졌어요.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"친구들과 함께한 카페 시간이 즐겁고 편안했습니다.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"새로 시작한 취미 활동이 생각보다 재미있고 만족스러워요.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"오랜만에 읽은 책이 마음에 위로가 되어 감사했습니다.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"주말 나들이에서 아름다운 풍경을 보며 힐링이 되었어요.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"좋아하는 드라마를 보며 웃고 울면서 스트레스가 해소되었습니다.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"반려동물과 함께하는 시간이 언제나 기쁨을 줍니다.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"요리를 하면서 새로운 레시피에 도전하는 것이 즐거웠어요.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"정원 가꾸기를 하며 식물들이 자라는 모습에 뿌듯함을 느꼈습니다.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"동네 산책로에서 만난 이웃들과의 인사가 따뜻했어요.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"집에서 보내는 여유로운 시간이 마음의 평화를 가져다줍니다.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"새로운 장소를 탐험하며 발견한 작은 기쁨들이 소중했어요.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"일상의 작은 변화들이 새로운 활력을 불어넣어 주었습니다.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"오랜 친구와의 만남에서 변함없는 우정을 확인할 수 있어 감사했어요.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"인간관계"
    }
  },
  {
    "content":"가족들과의 대화가 깊어지면서 더 가까워진 느낌이 듭니다.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"인간관계"
    }
  },
  {
    "content":"새로운 사람들과의 만남이 즐겁고 신선한 자극이 되었어요.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"인간관계"
    }
  },
  {
    "content":"동료의 배려심 깊은 행동에 마음이 따뜻해졌습니다.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"인간관계"
    }
  },
  {
    "content":"연인과 함께하는 시간이 언제나 행복하고 달콤해요.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"인간관계"
    }
  },
  {
    "content":"이웃과의 인사를 나누며 공동체 의식을 느꼈습니다.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"인간관계"
    }
  },
  {
    "content":"친구의 고민을 들어주면서 서로 위로가 되는 시간이었어요.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"인간관계"
    }
  },
  {
    "content":"가족 모임에서 웃음이 끊이지 않아 즐거웠습니다.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"인간관계"
    }
  },
  {
    "content":"새로운 취미 모임에서 좋은 사람들을 만나 기뻤어요.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"인간관계"
    }
  },
  {
    "content":"동료들과의 팀워크가 완벽해서 일하는 것이 즐거웠습니다.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"인간관계"
    }
  },
  {
    "content":"오랫동안 연락하지 못했던 친구로부터 안부 연락이 와서 반가웠어요.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"인간관계"
    }
  },
  {
    "content":"가족의 응원과 지지가 큰 힘이 되어 감동받았습니다.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"인간관계"
    }
  },
  {
    "content":"새로운 친구와의 공통 관심사를 발견해서 신나는 대화를 나눴어요.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"인간관계"
    }
  },
  {
    "content":"동료의 성공을 함께 기뻐하며 진심으로 축하할 수 있어 뿌듯했습니다.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"인간관계"
    }
  },
  {
    "content":"멀리 있는 가족과 화상통화로 얼굴을 보니 그리움이 해소되었어요.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"인간관계"
    }
  },
  {
    "content":"계획했던 저축 목표를 달성해서 뿌듯하고 안정감을 느꼈어요.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"합리적인 쇼핑으로 필요한 물건을 구매해서 만족스럽습니다.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"투자 수익이 생겨서 경제적 여유가 생긴 것이 기뻐요.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"가계부 정리를 통해 가계 관리가 체계적으로 되어 안심됩니다.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"할인 혜택을 잘 활용해서 현명한 소비를 한 것 같아 뿌듯해요.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"부업을 통한 추가 수입이 생겨서 경제적 자유도가 높아졌습니다.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"원하던 물건을 드디어 구매할 수 있어서 정말 기뻤어요.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"예산 관리를 잘해서 여행 자금을 모을 수 있게 되어 기대됩니다.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"중고 거래로 불필요한 물건을 정리하면서 공간도 깔끔해졌어요.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"적금이 만기되어 목돈이 생긴 것이 든든하고 안정적입니다.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"가족과 함께 경제 교육을 받으며 재정 관리 지식이 늘었어요.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"새로운 적립식 상품에 가입해서 미래를 준비하는 기분입니다.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"생활비 절약에 성공해서 여유 자금이 생긴 것이 뿌듯해요.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"온라인 쇼핑몰에서 좋은 상품을 저렴하게 구매해서 만족스럽습니다.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"금융 상품 비교를 통해 더 유리한 조건을 찾아 갈아탔어요.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"오늘 프로젝트를 성공적으로 마무리해서 성취감이 넘쳐납니다.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"새로운 기술을 배우면서 성장하는 느낌이 정말 기뻐요.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"동료들과의 협업이 순조롭게 진행되어 만족스럽습니다.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"상사로부터 받은 긍정적인 피드백이 큰 동기부여가 되었어요.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"어려운 문제를 해결했을 때의 짜릿함이 최고였습니다.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"새로운 프로젝트에 참여하게 되어 설레고 기대됩니다.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"교육과정을 통해 얻은 지식이 실무에 도움이 되어 뿌듯해요.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"팀원들과 함께 목표를 달성한 순간이 감동적이었습니다.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"창의적인 아이디어가 떠올라 흥미진진한 하루였어요.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"업무 효율성이 향상되어 여유 시간이 생긴 것이 기쁩니다.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"새로운 언어를 배우면서 점점 실력이 늘어가는 것이 즐거워요.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"온라인 강의를 통해 전문성을 키워가는 과정이 보람됩니다.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"멘토의 조언이 큰 도움이 되어 감사한 마음입니다.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"업무상 네트워킹을 통해 좋은 인연을 만나게 되어 기뻤어요.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"자기계발서를 읽으며 새로운 관점을 얻어 영감을 받았습니다.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"꾸준한 운동으로 체력이 향상되어 활기찬 하루를 보냈어요.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"건강검진 결과가 좋아서 안심이 되고 기뻤습니다.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"규칙적인 수면 패턴을 유지하니 컨디션이 훨씬 좋아졌어요.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"새로운 운동을 시작하면서 몸과 마음이 건강해지는 느낌입니다.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"균형 잡힌 식단을 통해 에너지가 넘치는 하루였어요.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"명상과 요가를 통해 마음의 평정을 찾을 수 있었습니다.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"의사 선생님의 친절한 설명 덕분에 건강 관리에 자신감이 생겼어요.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"금연\/금주에 성공하면서 몸이 한결 가벼워진 기분입니다.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"정기적인 산책이 스트레스 해소에 큰 도움이 되고 있어요.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"건강한 취미 활동을 통해 삶의 질이 향상되었습니다.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"친구들과 함께하는 운동이 즐겁고 동기부여가 되어요.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"몸무게 감량 목표를 달성해서 성취감과 자신감이 생겼습니다.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"새로운 건강 습관을 만들어가는 과정이 보람됩니다.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"체력 증진으로 일상생활이 더욱 활동적으로 변했어요.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"마음 건강을 위한 취미 활동이 큰 위로가 되고 있습니다.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"생일을 맞아 가족과 친구들의 축하를 받으며 행복한 하루였어요.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"결혼기념일을 기념하며 연인과 특별한 시간을 보냈습니다.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"졸업식에서 그동안의 노력이 결실을 맺어 감격스러웠어요.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"승진 소식을 듣고 그동안의 노고가 인정받는 기분이었습니다.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"새해 첫날 새로운 목표를 세우며 희망찬 마음이 들었어요.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"크리스마스 가족 모임에서 따뜻한 사랑을 느꼈습니다.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"친구의 결혼식에 참석해서 행복한 순간을 함께 나눴어요.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"첫 직장 입사일에 새로운 시작에 대한 설렘이 가득했습니다.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"시험 합격 소식을 들으며 노력의 보람을 느꼈어요.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"가족 여행에서 만든 추억들이 평생 잊을 수 없을 것 같아요.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"아이의 첫 걸음마를 보며 감동의 눈물을 흘렸습니다.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"새집으로 이사하면서 새로운 환경에 대한 기대감이 컸어요.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"오랫동안 준비한 공연이 성공적으로 끝나 성취감이 넘쳤습니다.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"부모님의 환갑 잔치를 성공적으로 준비해 뿌듯했어요.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"새로운 반려동물을 입양하며 새 가족을 맞이하는 기쁨을 느꼈습니다.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"새로운 앱을 사용해보니 일상이 더 편리해져서 만족스러워요.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"온라인 강의를 통해 새로운 지식을 습득하는 것이 즐겁습니다.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"SNS에서 좋은 사람들과 소통하며 네트워킹이 확장되었어요.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"온라인 게임에서 친구들과 즐거운 시간을 보냈습니다.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"유튜브 영상 제작이 생각보다 재미있고 창의적인 활동이에요.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"온라인 쇼핑으로 원하던 상품을 편리하게 구매할 수 있어 좋았어요.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"화상회의 기술 덕분에 원격 근무가 효율적으로 가능해졌습니다.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"디지털 사진 편집을 배우면서 새로운 취미를 발견했어요.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"온라인 커뮤니티에서 같은 관심사를 가진 사람들을 만나 기뻤습니다.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"스마트폰 앱으로 건강 관리를 체계적으로 할 수 있게 되었어요.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"온라인 독서 모임에 참여하며 책에 대한 깊은 토론을 나눴습니다.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"디지털 기기 활용법을 익혀 업무 효율성이 크게 향상되었어요.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"온라인 블로그 운영을 통해 글쓰기 실력이 늘어가고 있습니다.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"가상현실 체험이 신기하고 미래적인 느낌이 들어 흥미로웠어요.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"온라인 금융 서비스 덕분에 banking이 훨씬 편리해졌습니다.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"명상을 통해 마음의 평정을 찾고 내면의 평화를 느꼈어요.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"일기 쓰기를 통해 하루를 돌아보며 감사한 마음이 들었습니다.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"자기 성찰 시간을 가지면서 개인적 성장을 실감했어요.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"긍정적인 생각으로 마음을 다스리니 기분이 한결 밝아졌습니다.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"내가 진정으로 원하는 것이 무엇인지 깨달아 명확해졌어요.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"감사 인사를 표현하며 마음이 따뜻해지는 것을 느꼈습니다.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"과거의 아픈 기억을 용서하고 놓아주니 마음이 가벼워졌어요.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"자신감을 회복하면서 새로운 도전에 대한 용기가 생겼습니다.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"스트레스를 건강하게 해소하는 방법을 찾아 마음이 편해졌어요.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"내면의 목소리에 귀 기울이며 진정한 나를 발견했습니다.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"부정적인 감정을 인정하고 받아들이니 오히려 평온해졌어요.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"자기 자신을 사랑하는 법을 배우며 자존감이 높아졌습니다.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"마음의 여유를 찾으면서 삶에 대한 만족도가 올라갔어요.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"내적 동기를 발견하며 목표 달성에 대한 의지가 강해졌습니다.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"감정 조절 능력이 향상되어 대인관계가 더 원활해졌어요.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"새로운 그림을 완성하며 창작의 기쁨을 만끽했어요.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"글쓰기 실력이 늘어가는 것을 느끼며 성장의 기쁨을 맛봤습니다.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"요리 레시피를 창조하면서 창의성을 발휘하는 것이 즐거웠어요.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"새로운 언어를 배우며 소통의 폭이 넓어지는 기분입니다.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"악기 연주 실력이 향상되어 음악적 표현력이 풍부해졌어요.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"DIY 프로젝트를 완성하며 손으로 만드는 즐거움을 느꼈습니다.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"새로운 기술을 습득하면서 전문성이 깊어지는 것 같아요.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"창작 활동을 통해 스트레스가 해소되고 마음이 정화되었습니다.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"개인 프로젝트를 시작하며 새로운 도전에 설레는 마음이에요.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"예술 작품을 감상하며 영감과 감동을 받았습니다.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"새로운 분야에 도전하면서 가능성의 확장을 경험했어요.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"창작물에 대한 긍정적인 피드백을 받아 동기부여가 되었습니다.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"예술적 감성이 발달하면서 세상을 보는 시각이 풍부해졌어요.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"창의적 문제 해결 능력이 향상되어 업무에도 도움이 되고 있습니다.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"자신만의 작품 세계를 구축해가는 과정이 매우 보람됩니다.",
    "metadata":{
      "emotion":"긍정적 감정",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"계획했던 주말 나들이가 비 때문에 취소되어 실망스럽고 우울해요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"집안일이 너무 많이 쌓여서 압박감을 느끼고 스트레스받습니다.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"좋아하던 TV 프로그램이 종영되어 허전하고 아쉬운 마음이에요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"반려동물이 아파서 걱정이 되고 마음이 무거워요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"일상이 너무 반복적이라 지루하고 무기력한 기분입니다.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"요리를 하다가 실패해서 짜증나고 자신감이 떨어져요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"휴일인데도 제대로 쉬지 못해 피로하고 답답합니다.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"친구들과의 약속이 갑자기 취소되어 서운하고 외로워요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"집 주변 공사 소음 때문에 예민해지고 화가 나요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"계절 변화로 몸이 적응하지 못해 컨디션이 안 좋아요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"취미 활동을 할 시간이 없어서 답답하고 불만스럽습니다.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"가전제품이 고장나서 불편하고 당황스러워요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"날씨가 계속 흐려서 기분도 우울하고 무기력해집니다.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"동네 환경이 변해서 적응하기 어렵고 불편해요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"여가 시간에도 일 생각이 나서 제대로 쉬지 못해 스트레스받아요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"계속되는 두통 때문에 일상생활이 힘들고 짜증이 나요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"건강검진에서 이상 소견이 나와서 불안하고 걱정됩니다.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"만성 피로로 인해 무기력하고 삶의 의욕이 떨어져요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"잠을 제대로 못 자서 컨디션이 안 좋고 예민해집니다.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"스트레스성 질환이 생겨서 몸과 마음이 모두 힘들어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"운동 부족으로 체력이 떨어져서 자책감과 우울감을 느껴요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"병원비 부담 때문에 치료를 망설이게 되어 스트레스받습니다.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"약물 부작용으로 인해 일상생활에 지장이 생겨서 답답해요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"생활 습관을 바꾸기 어려워서 건강 관리에 실패감을 느껴요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"가족의 건강 문제 때문에 걱정이 많아지고 마음이 무거워요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"다이어트에 번번이 실패해서 자신감이 떨어지고 우울해요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"원인 모를 증상 때문에 의료진을 전전하며 불안감이 커져요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"정신적 스트레스가 신체 증상으로 나타나서 괴로워요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"건강한 생활을 유지하기 어려운 환경 때문에 좌절감을 느껴요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"나이 들면서 신체 기능이 떨어지는 것에 대한 두려움이 있어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"인터넷 연결이 불안정해서 중요한 업무에 차질이 생겨 스트레스받아요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"SNS에서 악플을 받아서 상처받고 우울한 마음이 들어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"온라인 쇼핑에서 사기를 당해서 분하고 억울한 기분입니다.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"스마트폰 중독 때문에 일상생활에 지장이 생겨서 자책감을 느껴요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"화상회의 기술 문제로 중요한 미팅이 망쳐져서 당황스럽고 화가 나요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"개인정보 유출 사고로 인해 불안하고 걱정이 많아져요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"온라인 게임에서 계속 패배해서 짜증나고 좌절감을 느껴요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"디지털 기기 사용법을 몰라서 소외감과 답답함을 느낍니다.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"온라인 커뮤니티에서 논쟁에 휘말려서 스트레스받고 피곤해요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"사이버 괴롭힘을 당해서 인터넷 사용이 두렵고 위축돼요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"온라인 강의 집중이 안 되어서 학습 효율이 떨어져 불안해요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"디지털 기기 고장으로 중요한 데이터를 잃어서 절망스러워요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"온라인에서 가짜 뉴스에 속아서 혼란스럽고 화가 나요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"과도한 화면 시청으로 눈이 피로해서 건강이 걱정돼요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"디지털 격차로 인해 정보 접근에 어려움을 느끼고 소외감이 들어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"프로젝트 마감에 쫓겨 밤늦게까지 일해서 지치고 스트레스받아요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"상사의 무리한 요구 때문에 화가 나고 억울한 마음입니다.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"새로운 업무를 배우는 것이 어려워서 불안하고 자신감이 없어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"동료와의 갈등으로 인해 직장 생활이 힘들고 우울합니다.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"업무량이 너무 많아서 과로에 시달리고 번아웃을 느껴요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"승진에서 누락되어 실망스럽고 좌절감을 느낍니다.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"실수로 인한 손실 때문에 죄책감과 후회가 밀려와요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"회사 분위기가 경직되어 있어서 숨이 막히고 답답해요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"새로운 시스템 적응이 어려워서 업무 효율이 떨어져 스트레스받아요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"학습 진도가 늦어져서 조급하고 불안한 마음입니다.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"시험 결과가 기대에 못 미쳐서 실망하고 자책하고 있어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"직장 내 인간관계 때문에 출근하기 싫고 우울해요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"업무 관련 교육이 이해되지 않아서 좌절감을 느낍니다.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"야근이 계속되어서 피로하고 개인 시간이 없어 화가 나요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"경력 발전이 정체된 것 같아서 불안하고 초조합니다.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"예상치 못한 지출로 인해 가계 부담이 커져서 스트레스받아요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"투자에서 손실이 발생해서 후회되고 불안한 마음입니다.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"월급이 부족해서 생활비 걱정에 잠 못 이루는 밤이 많아요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"사고 싶은 물건을 살 여유가 없어서 박탈감과 서운함을 느껴요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"대출 상환 부담 때문에 미래에 대한 불안감이 커져요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"물가 상승으로 인해 생활 수준이 떨어져서 우울하고 화가 나요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"충동구매 후 후회가 밀려와서 자책하고 있습니다.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"경제적 여유 없음으로 인해 사회 활동에 제약이 생겨서 위축돼요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"가족의 경제적 요구에 부응하지 못해서 미안하고 무력감을 느껴요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"적금을 깨야 하는 상황이 생겨서 계획이 틀어져 좌절스러워요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"사기를 당해서 경제적 손실과 함께 정신적 충격이 커요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"친구들과의 경제적 격차 때문에 모임 참여가 부담스러워요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"노후 준비가 부족한 것 같아서 불안하고 초조한 마음이에요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"신용 관리 실수로 인한 불이익이 생겨서 후회되고 스트레스받아요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"경제 불황으로 인한 불안정한 미래가 걱정되고 우울해요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"자존감이 낮아져서 모든 일에 자신감이 없고 위축되는 기분이에요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"과거의 실수가 계속 떠올라서 후회와 자책감에 시달려요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"미래에 대한 불안감이 커서 잠 못 이루는 밤이 많아져요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"우울감이 지속되어서 일상생활에 의욕이 생기지 않아요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"분노를 조절하지 못해서 주변 사람들과의 관계가 악화되고 있어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"완벽주의 성향 때문에 스스로를 너무 압박해서 괴로워요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"외로움이 깊어져서 세상과 단절된 느낌이 들어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"질투심과 열등감 때문에 마음이 괴롭고 평정을 잃어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"스트레스가 누적되어서 감정 기복이 심해지고 예민해져요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"자기 혐오감이 들어서 거울 보는 것도 힘들고 우울해요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"내면의 갈등으로 인해 결정을 내리지 못하고 혼란스러워요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"의미 없는 일상의 반복으로 삶의 목적을 잃은 것 같아 공허해요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"타인의 시선을 의식하느라 진정한 나를 잃어가는 것 같아요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"감정 표현이 서툴러서 소통에 어려움을 겪고 답답해요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"부정적인 생각의 악순환에 빠져서 헤어나오지 못하고 있어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"가까운 친구와 다툰 후 관계가 어색해져서 마음이 무거워요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"인간관계"
    }
  },
  {
    "content":"가족 간의 의견 차이로 갈등이 생겨서 스트레스받고 있습니다.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"인간관계"
    }
  },
  {
    "content":"연인과의 관계에서 오해가 생겨 불안하고 서운한 마음이에요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"인간관계"
    }
  },
  {
    "content":"새로운 환경에서 사람들과 어울리지 못해 외롭고 소외감을 느껴요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"인간관계"
    }
  },
  {
    "content":"동료의 배신감 있는 행동 때문에 신뢰가 깨져서 상처받았어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"인간관계"
    }
  },
  {
    "content":"가족의 무관심 때문에 서운하고 혼자라는 느낌이 듭니다.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"인간관계"
    }
  },
  {
    "content":"친구들 사이에서 끼지 못하는 느낌이 들어서 위축되고 슬퍼요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"인간관계"
    }
  },
  {
    "content":"이웃과의 갈등으로 인해 집에 있는 것도 불편하고 스트레스받아요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"인간관계"
    }
  },
  {
    "content":"SNS에서 친구들의 행복한 모습을 보니 상대적 박탈감을 느껴요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"인간관계"
    }
  },
  {
    "content":"중요한 사람으로부터 연락이 없어서 불안하고 걱정돼요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"인간관계"
    }
  },
  {
    "content":"사회적 모임에서 소외당하는 느낌이 들어서 자존감이 떨어져요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"인간관계"
    }
  },
  {
    "content":"가족의 과도한 간섭 때문에 답답하고 자유롭지 못한 기분이에요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"인간관계"
    }
  },
  {
    "content":"친구의 성공을 보니 질투심과 열등감이 생겨서 혼란스러워요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"인간관계"
    }
  },
  {
    "content":"대인관계에서 자꾸 상처받아서 사람들과 거리를 두고 싶어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"인간관계"
    }
  },
  {
    "content":"오해로 인한 관계 악화가 풀리지 않아서 답답하고 속상합니다.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"인간관계"
    }
  },
  {
    "content":"생일인데 아무도 기억해주지 않아서 외롭고 서운한 마음이에요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"중요한 시험에 떨어져서 좌절감과 실망감이 클러워요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"결혼기념일인데 연인과 다퉈서 마음이 복잡하고 슬퍼요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"가족 모임에서 갈등이 생겨서 명절이 괴롭고 스트레스받아요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"오랫동안 준비한 행사가 실패해서 허탈하고 자책감이 들어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"졸업식 날 진로에 대한 불안감으로 기쁘기보다 걱정이 앞서요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"새해가 왔지만 달라질 것 없는 현실에 우울하고 무기력해요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"승진 기회를 놓쳐서 동료들 앞에서 창피하고 분하는 마음이에요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"크리스마스에 혼자 있게 되어서 외로움과 소외감을 크게 느껴요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"이사 과정에서 여러 문제가 생겨서 스트레스받고 후회돼요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"결혼식 준비가 예상보다 어려워서 불안하고 압박감을 느껴요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"부모님의 건강 악화로 가족 행사가 취소되어서 마음이 무거워요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"입학식 날 새로운 환경에 대한 두려움과 불안감이 커요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"퇴사일에 아쉬움보다 미래에 대한 불확실성 때문에 걱정돼요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"기념일에 계획했던 일들이 모두 틀어져서 실망스럽고 화가 나요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"창작 활동에서 슬럼프에 빠져서 아이디어가 나오지 않아 좌절스러워요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"작품에 대한 혹평을 받아서 자신감이 떨어지고 상처받았어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"새로운 기술 습득이 어려워서 포기하고 싶은 마음이 들어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"창작물이 예상과 다르게 나와서 실망스럽고 자책하고 있어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"다른 사람의 뛰어난 작품을 보니 열등감과 질투심이 생겨요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"창작 시간을 확보하지 못해서 꿈을 포기해야 할까 고민돼요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"예술적 재능이 부족한 것 같아서 자신에 대해 회의감이 들어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"창작 활동에 대한 주변의 무관심으로 외롭고 서운한 마음이에요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"완벽한 작품을 만들어야 한다는 압박감 때문에 시작조차 못하고 있어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"창작 과정에서 계속 실패만 반복해서 의욕이 사라져가요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"새로운 분야에 도전했지만 실력 부족을 느껴서 위축돼요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"창작물에 대한 비판을 받아들이기 어려워서 성장이 막힌 것 같아요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"예술적 영감이 마른 것 같아서 앞으로가 막막하고 불안해요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"창작 활동의 경제적 불안정성 때문에 고민이 많아져요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"자신만의 독창적인 스타일을 찾지 못해서 혼란스럽고 답답해요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"집에 혼자 있을 때 이상한 소리가 들려서 무서워서 떨고 있어요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"어둠 속에서 길을 걸을 때마다 뒤에서 누가 따라오는 것 같아 두려워요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"엘리베이터에 갇힐까 봐 무서워서 계단만 이용하고 있습니다.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"높은 곳에 올라가면 떨어질 것 같은 공포감에 다리가 후들거려요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"반려동물이 갑자기 아플까 봐 항상 불안하고 걱정이 많아요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"번개와 천둥소리가 너무 무서워서 비 오는 날은 밖에 나가기 두려워요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"대중교통을 이용할 때 사고가 날까 봐 항상 긴장하고 있어요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"수영장에 가고 싶지만 물에 빠질까 봐 두려워서 망설여져요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"밤에 잠들기 전 집 안 보안이 걱정되어 계속 확인하게 돼요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"벌레나 뱀 같은 동물을 보면 소리를 지르며 도망가고 싶어져요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"놀이공원의 무서운 놀이기구는 상상만 해도 공포스러워요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"집 주변에서 일어나는 범죄 소식을 들으면 밖에 나가기 무서워요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"요리할 때 가스레인지 사용이 두려워서 항상 조심스러워요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"무서운 영화나 드라마는 절대 보지 못하겠어요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"계절이 바뀔 때마다 날씨 변화가 몸에 미칠 영향이 걱정돼요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"작은 증상도 큰 병일까 봐 무서워서 병원에 가기 두려워요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"수술이나 시술을 받아야 한다는 말에 공포감이 밀려와요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"유전적 질병을 물려받을까 봐 미래에 대한 불안이 커져요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"건강검진 결과를 받기 전까지 며칠 동안 잠을 못 자요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"응급실에 혼자 가야 할 상황이 생기면 무섭고 당황스러워요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"주사나 채혈이 너무 무서워서 의료진을 피하고 싶어져요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"갑작스런 심장 두근거림이 심장병일까 봐 공포에 떨어요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"가족력이 있는 질병에 걸릴까 봐 항상 불안하고 예민해요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"병원에서 나쁜 소식을 들을까 봐 진료 예약을 미루고 있어요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"응급상황에서 혼자 대처하지 못할까 봐 외출이 두려워요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"약물 부작용이나 알레르기 반응이 생길까 봐 걱정돼요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"정신건강 문제로 낙인찍힐까 봐 상담받기를 망설여요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"나이가 들면서 몸이 아플까 봐 미래에 대한 공포가 있어요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"의료비 부담 때문에 치료를 제대로 받지 못할까 봐 무서워요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"치과 치료가 너무 무서워서 치아가 아파도 참고 있어요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"해킹당해서 개인정보가 유출될까 봐 온라인 활동이 무서워요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"인터넷 뱅킹 사용 중 피싱 사기에 당할까 봐 항상 조심스러워요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"SNS에 올린 사진이나 글이 악용될까 봐 포스팅하기 두려워요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"온라인 쇼핑에서 사기 쇼핑몰에 속을까 봐 구매를 망설여요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"컴퓨터 바이러스에 감염되어 모든 데이터를 잃을까 봐 무서워요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"사이버 괴롭힘을 당할까 봐 온라인 커뮤니티 활동을 피해요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"화상회의 중 실수해서 녹화된 영상이 퍼질까 봐 걱정돼요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"스마트폰을 분실해서 모든 정보가 노출될까 봐 불안해요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"온라인 게임에서 계정을 해킹당할까 봐 로그인하기 두려워요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"가짜 뉴스에 속아서 잘못된 정보를 퍼뜨릴까 봐 조심스러워요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"클라우드 서비스가 해킹당해서 사진들을 잃을까 봐 걱정돼요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"온라인 강의 중 카메라나 마이크 실수로 민망할까 봐 두려워요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"디지털 기기 조작을 잘못해서 중요한 파일을 삭제할까 봐 무서워요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"온라인 데이팅에서 위험한 사람을 만날까 봐 사용하기 두려워요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"AI 기술 발달로 내 일자리가 사라질까 봐 미래가 불안해요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"중요한 프레젠테이션 앞두고 실수할까 봐 밤잠을 이루지 못해요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"새로운 프로젝트를 맡게 되어 실패할까 봐 불안하고 두려워요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"상사에게 혼날까 봐 업무 보고를 할 때마다 가슴이 두근거려요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"회사 구조조정으로 해고당할까 봐 매일 불안에 떨고 있어요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"새로운 기술을 배워야 하는데 따라가지 못할까 봐 걱정돼요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"면접에서 떨어질까 봐 두려워서 제대로 대답하지 못했어요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"동료들 앞에서 발표할 때 시선이 무서워서 목소리가 떨려요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"업무 실수로 큰 손해를 입힐까 봐 항상 조마조마해요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"시험에서 낙제할까 봐 밤늦게까지 공부하느라 스트레스받아요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"새로운 직장 환경에 적응하지 못할까 봐 출근이 두려워요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"팀 프로젝트에서 다른 팀원들에게 피해를 줄까 봐 불안해요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"승진 기회를 놓칠까 봐 과도하게 자신을 압박하고 있어요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"중요한 회의에서 잘못된 의견을 말할까 봐 입을 열지 못해요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"학위 취득에 실패할까 봐 학업에 대한 부담감이 커져요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"경쟁이 치열한 직장에서 뒤처질까 봐 항상 긴장 상태예요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"갑작스런 실직으로 생계가 막막해질까 봐 항상 불안해요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"투자한 돈을 모두 잃을까 봐 밤잠을 이루지 못해요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"노후 준비가 부족해서 나중에 빈곤하게 살까 봐 두려워요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"큰 지출이 생겨서 빚을 지게 될까 봐 소비를 극도로 자제해요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"경제 불황으로 회사가 문을 닫을까 봐 걱정이 많아져요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"사기를 당해서 전 재산을 잃을까 봐 투자가 무서워요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"신용등급이 떨어져서 대출을 받지 못할까 봐 불안해요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"물가 상승으로 생활비가 감당 안 될까 봐 걱정돼요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"은행 계좌가 해킹당해서 돈을 잃을까 봐 온라인 뱅킹이 무서워요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"부모님 의료비로 인해 가정 경제가 파탄날까 봐 두려워요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"자녀 교육비를 감당하지 못할까 봐 미래가 막막해요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"집값 폭락으로 전세금을 잃을까 봐 부동산 시장이 무서워요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"갑작스런 사고로 큰 배상금을 물어야 할까 봐 걱정돼요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"카드 연체로 신용불량자가 될까 봐 항상 조마조마해요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"경제적 어려움으로 가족에게 피해를 줄까 봐 자책하고 있어요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"혼자 있을 때 떠오르는 어두운 생각들이 무섭고 통제가 안 돼요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"과거의 트라우마가 갑자기 떠올라서 패닉 상태가 돼요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"내가 정신적으로 문제가 있는 건 아닐까 봐 두려워요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"우울감이 더 심해져서 극단적인 선택을 할까 봐 무서워요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"분노를 조절하지 못해서 타인에게 해를 끼칠까 봐 걱정돼요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"불안 발작이 또 올까 봐 항상 긴장하고 조마조마해요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"내 진짜 모습이 들키면 모든 사람이 떠날까 봐 두려워요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"완벽하지 못한 내 모습을 타인이 발견할까 봐 숨기고 있어요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"자존감이 너무 낮아져서 아무것도 할 수 없을까 봐 무서워요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"외로움이 더 깊어져서 완전히 고립될까 봐 걱정돼요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"내 감정이 폭발해서 주변 사람들을 상처입힐까 봐 억누르고 있어요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"정신적으로 무너져서 일상생활을 못할까 봐 불안해요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"끔찍한 상상이나 강박적 사고에서 벗어나지 못할까 봐 두려워요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"내가 미쳐가는 건 아닐까 하는 생각에 공포스러워요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"마음의 병이 점점 악화되어 돌이킬 수 없게 될까 봐 걱정돼요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"새로운 사람들 앞에서 거부당할까 봐 말을 걸기가 두려워요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"인간관계"
    }
  },
  {
    "content":"가까운 사람이 날 떠날까 봐 불안해서 계속 확인하고 싶어져요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"인간관계"
    }
  },
  {
    "content":"갈등 상황에서 관계가 끝날까 봐 제대로 의견을 표현하지 못해요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"인간관계"
    }
  },
  {
    "content":"친구들 사이에서 따돌림당할까 봐 항상 눈치를 보게 돼요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"인간관계"
    }
  },
  {
    "content":"연인과의 관계에서 버림받을까 봐 불안하고 집착하게 돼요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"인간관계"
    }
  },
  {
    "content":"가족에게 실망을 안겨줄까 봐 진실을 말하기 두려워요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"인간관계"
    }
  },
  {
    "content":"사회적 모임에서 실수할까 봐 참석하기가 무서워요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"인간관계"
    }
  },
  {
    "content":"다른 사람들이 나를 어떻게 생각할지 몰라서 위축돼요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"인간관계"
    }
  },
  {
    "content":"친구에게 도움을 요청했다가 거절당할까 봐 혼자 해결하려 해요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"인간관계"
    }
  },
  {
    "content":"대화에서 무시당할까 봐 자신의 의견을 숨기게 돼요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"인간관계"
    }
  },
  {
    "content":"SNS에 글을 올렸다가 비판받을까 봐 삭제하고 싶어져요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"인간관계"
    }
  },
  {
    "content":"새로운 환경에서 친구를 사귀지 못할까 봐 걱정이 많아요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"인간관계"
    }
  },
  {
    "content":"가족 모임에서 비교당할까 봐 참석하기 싫어져요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"인간관계"
    }
  },
  {
    "content":"동료들과의 경쟁에서 밀릴까 봐 관계 형성이 어려워요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"인간관계"
    }
  },
  {
    "content":"과거의 실수가 알려져서 평판이 나빠질까 봐 두려워요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"인간관계"
    }
  },
  {
    "content":"결혼식 당일 실수할까 봐 며칠 전부터 잠을 못 자고 있어요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"입학시험 결과 발표일이 다가올수록 불안감이 커져요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"면접 당일 준비한 것을 다 잊어버릴까 봐 공포스러워요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"졸업 후 진로가 정해지지 않아서 미래가 두려워요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"중요한 발표회에서 실패할까 봐 연습할 때마다 떨려요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"가족 행사에서 갈등이 생길까 봐 참석하기 싫어져요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"생일파티를 열었다가 아무도 오지 않을까 봐 걱정돼요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"이사 과정에서 물건을 분실하거나 파손될까 봐 무서워요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"첫 출근일에 실수해서 첫인상을 망칠까 봐 불안해요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"운전면허 시험에서 또 떨어질까 봐 시험장 가기가 두려워요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"여행 중 사고나 사건에 휘말릴까 봐 외국 가기가 무서워요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"중요한 시상식에서 상을 받지 못할까 봐 기대하기 두려워요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"새로운 집으로 이사 후 동네에 적응하지 못할까 봐 걱정돼요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"퇴직 후 새로운 삶을 시작하는 것이 막막하고 두려워요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"가족의 중요한 수술 날짜가 다가올수록 공포감이 커져요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"새로운 도전을 했다가 완전히 실패할까 봐 시작하기 두려워요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"내 작품이 혹평을 받아서 창작 의욕을 잃을까 봐 무서워요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"재능이 부족해서 꿈을 포기해야 할까 봐 불안해요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"창작 과정에서 영감이 완전히 마를까 봐 걱정되고 두려워요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"다른 작가들과 비교당해서 실력 부족이 드러날까 봐 위축돼요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"새로운 기술을 배우다가 따라가지 못할까 봐 도전이 무서워요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"작품 발표 후 아무도 관심을 보이지 않을까 봐 공개하기 두려워요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"창작 활동으로 생계를 이어가지 못할까 봐 현실적 두려움이 있어요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"슬럼프에서 벗어나지 못해서 영원히 못 쓸까 봐 공포스러워요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"표절 시비에 휘말려서 창작자로서 매장될까 봐 걱정돼요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"새로운 장르에 도전했다가 기존 팬들을 잃을까 봐 망설여져요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"창작물이 상업적으로 실패해서 다음 기회를 잃을까 봐 불안해요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"비판에 너무 민감해서 창작 활동을 지속하지 못할까 봐 두려워요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"나이가 들면서 창의력이 떨어질까 봐 시간에 쫓기는 기분이에요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"완벽한 작품을 만들지 못할까 봐 완성하지 못하고 있어요.",
    "metadata":{
      "emotion":"두려움과 공포",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"주말 계획을 세우는데 뭔가 잘못될 것 같아서 계속 불안해요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"친구들과의 약속 시간이 다가올수록 긴장되고 초조해져요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"새로운 취미를 시작하려고 하는데 잘 못할까 봐 망설여져요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"여행 준비를 하면서 빠뜨린 게 있을까 봐 계속 체크하게 돼요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"운전할 때마다 사고가 날까 봐 온몸에 힘이 들어가고 긴장돼요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"새로운 동네로 이사 후 적응하지 못할까 봐 불안감이 커져요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"반려동물 건강이 걱정되어서 작은 변화에도 예민하게 반응해요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"집을 비울 때마다 문을 제대로 잠갔는지 계속 확인하러 가요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"날씨 변화에 민감해져서 기상예보를 하루 종일 체크하고 있어요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"쇼핑할 때 잘못된 선택을 할까 봐 결정하지 못하고 망설여요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"요리를 할 때 실패할까 봐 레시피를 여러 번 확인하게 돼요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"외출 전 준비하면서 뭔가 빠뜨릴까 봐 계속 점검하느라 지쳐요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"가전제품 사용할 때마다 고장날까 봐 조심스럽고 긴장돼요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"휴일에도 마음이 편하지 않고 뭔가 해야 할 것 같아 불안해요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"일상의 작은 변화에도 적응하기 어려워서 스트레스받고 있어요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"건강검진 날짜가 다가올수록 결과가 걱정되어서 잠을 못 자요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"몸에 작은 이상이 생기면 큰 병의 전조증상일까 봐 불안해져요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"병원 예약을 하고 나서 진료받을 때까지 계속 긴장 상태가 돼요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"새로운 약을 처방받으면 부작용이 생길까 봐 복용하기 전에 망설여요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"가족력이 있는 질병에 대해 생각하면 미래가 불안하고 걱정돼요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"운동을 시작하려 하는데 몸에 무리가 갈까 봐 조심스러워요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"수술이나 시술을 앞두고 있어서 며칠 전부터 잠이 안 와요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"정기 검진 결과를 기다리는 동안 온갖 걱정이 머릿속을 맴돌아요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"응급실에 가야 할 상황에서 혼자 대처할 수 있을지 불안해요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"새로운 의료진과 첫 진료를 받을 때 제대로 설명할 수 있을지 걱정돼요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"건강 관리를 제대로 하지 못하는 것 같아서 자책하며 불안해요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"컨디션이 안 좋은 날이 계속되면 만성질환일까 봐 걱정돼요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"의료비 부담 때문에 필요한 치료를 받지 못할까 봐 스트레스받아요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"건강 정보를 검색하다 보면 더 큰 불안감에 휩싸이게 돼요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"나이가 들면서 건강이 악화될까 봐 미래에 대한 걱정이 커져요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"중요한 파일을 클라우드에 업로드할 때 제대로 저장될까 봐 긴장돼요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"온라인 쇼핑에서 결제할 때마다 보안이 걱정되어서 망설여요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"SNS에 게시물을 올리기 전에 어떤 반응이 올지 몰라서 불안해요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"화상회의 전에 기술적 문제가 생길까 봐 미리 여러 번 테스트해요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"온라인 뱅킹 사용할 때마다 해킹당할까 봐 조심스럽고 긴장돼요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"이메일을 보내기 전에 오타나 실수가 있을까 봐 여러 번 확인해요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"새로운 앱이나 프로그램을 설치할 때 바이러스가 있을까 봐 걱정돼요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"온라인 미팅에서 음성이나 화면 문제가 생길까 봐 사전에 불안해요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"디지털 기기 업데이트할 때 데이터 손실이 있을까 봐 망설여요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"비밀번호를 변경하고 나서 제대로 저장됐는지 계속 확인하게 돼요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"온라인 게임이나 앱에서 계정 문제가 생길까 봐 조심스러워요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"인터넷 속도가 느려지면 중요한 작업이 중단될까 봐 긴장돼요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"소셜미디어에서 논란에 휘말릴까 봐 댓글 달기를 망설이게 돼요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"온라인 강의나 웨비나 참여 전에 준비가 부족할까 봐 불안해요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"디지털 기기가 갑자기 고장날까 봐 중요한 데이터를 자주 백업해요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"월요일이 다가올수록 주말에도 마음이 편하지 않고 불안해요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"새로운 프로젝트를 맡게 되어서 밤잠을 설치며 걱정하고 있어요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"회의 시간이 가까워질수록 가슴이 두근거리고 손에 땀이 나요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"업무 메일을 확인할 때마다 나쁜 소식이 있을까 봐 긴장돼요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"상사와 일대일 면담이 있어서 며칠 전부터 잠을 못 자고 있어요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"시험 날짜가 정해지니까 공부에 집중이 안 되고 초조해져요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"새로운 업무 시스템을 배워야 해서 적응할 수 있을지 불안해요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"동료들의 실력과 비교되는 상황에서 뒤처질까 봐 긴장돼요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"중요한 마감일이 다가오면서 완벽하게 할 수 있을지 걱정돼요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"온라인 강의를 들을 때 다른 사람들보다 늦을까 봐 조급해져요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"업무 성과 평가가 있어서 결과가 나올 때까지 불안하고 예민해요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"새로운 직장 환경에 적응하느라 매일 긴장 상태로 출근해요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"팀 프로젝트에서 내 역할을 제대로 못할까 봐 밤새 고민해요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"발표 순서가 가까워질수록 목소리가 떨리고 손이 떨려요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"업무량이 많아질 때마다 제시간에 끝낼 수 있을지 불안해요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"큰 금액을 쓸 때마다 나중에 후회할까 봐 결정하기 어려워요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"투자한 돈의 수익률을 하루에도 몇 번씩 확인하며 조바심이 나요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"월말이 다가올수록 생활비가 부족할까 봐 지출을 체크하게 돼요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"새로운 금융상품을 가입할 때 손해 볼까 봐 며칠 동안 고민해요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"카드 사용 후 연체될까 봐 자꾸 결제일을 확인하게 돼요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"경제 뉴스를 볼 때마다 내 재정에 미칠 영향이 걱정돼요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"온라인 쇼핑에서 결제 버튼을 누르기 전에 항상 망설이게 돼요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"적금 만기일이 다가오면 어떻게 재투자할지 몰라서 스트레스받아요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"가계부를 정리할 때마다 예상보다 많이 썼을까 봐 불안해요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"보험료 납입일이 가까워지면 계속 체크하며 빠뜨릴까 봐 걱정해요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"대출 심사 결과를 기다리는 동안 승인받을 수 있을지 초조해요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"전세 계약 갱신 시기가 되면 조건이 악화될까 봐 미리 걱정해요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"가족 경조사비나 선물비 지출이 예상되면 부담스럽고 긴장돼요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"세금 신고 기간이 되면 빠뜨린 항목이 있을까 봐 예민해져요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"은퇴 후 생활비가 부족할까 봐 노후 준비에 대한 불안이 커져요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"새로운 프로젝트를 시작할 때마다 완성하지 못할까 봐 불안해요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"창작물에 대한 영감이 떠오르지 않으면 재능이 없는 건 아닐까 걱정돼요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"작품을 공개하기 전에 다른 사람들의 반응이 어떨지 몰라서 긴장돼요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"새로운 기술이나 스킬을 배울 때 다른 사람만큼 못할까 봐 위축돼요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"창작 과정에서 막힐 때마다 이대로 포기해야 하나 싶어서 초조해져요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"다른 창작자들의 뛰어난 작품을 보면 내 실력이 부족한 것 같아 불안해요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"중요한 포트폴리오나 작품집을 준비할 때 완벽하지 않을까 봐 걱정돼요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"새로운 장르나 스타일에 도전할 때 실패할까 봐 시작하기 전에 망설여요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"창작 활동에 충분한 시간을 투자하지 못할까 봐 일정 관리에 스트레스받아요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"비판이나 피드백을 받을 때 감정적으로 상처받을까 봐 미리 긴장돼요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"창작물의 질이 예전만 못한 것 같아서 실력이 퇴보한 건 아닐까 걱정돼요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"아이디어를 구현하는 과정에서 기술적 한계에 부딪힐까 봐 불안해요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"창작 활동의 지속가능성에 대한 의문이 들어서 미래가 불확실하게 느껴져요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"완벽한 작품을 만들어야 한다는 압박감 때문에 중간에 포기하고 싶어져요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"성장 속도가 더딘 것 같아서 목표를 달성할 수 있을지 의구심이 들어요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"새로운 사람들과 만날 때마다 어떤 인상을 줄지 몰라서 긴장돼요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"인간관계"
    }
  },
  {
    "content":"친구와 약속이 있으면 대화가 어색할까 봐 미리 걱정하게 돼요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"인간관계"
    }
  },
  {
    "content":"가족 모임에서 비교당하거나 잔소리 들을까 봐 불안해요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"인간관계"
    }
  },
  {
    "content":"연인과의 관계에서 작은 변화에도 민감하게 반응하고 걱정해요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"인간관계"
    }
  },
  {
    "content":"동료들과의 점심 시간이 부담스럽고 어색한 침묵이 올까 봐 긴장돼요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"인간관계"
    }
  },
  {
    "content":"SNS에 글을 올리기 전에 다른 사람들 반응이 걱정되어 망설여요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"인간관계"
    }
  },
  {
    "content":"전화가 오면 나쁜 소식일까 봐 받기 전에 잠시 망설이게 돼요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"인간관계"
    }
  },
  {
    "content":"그룹 채팅에서 내 메시지가 무시당할까 봐 보내기 전에 고민해요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"인간관계"
    }
  },
  {
    "content":"파티나 모임에 가기 전에 어울리지 못할까 봐 며칠 전부터 걱정해요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"인간관계"
    }
  },
  {
    "content":"갈등 상황에서 어떻게 대응해야 할지 몰라서 계속 긴장 상태예요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"인간관계"
    }
  },
  {
    "content":"친구가 늦게 답장하면 혹시 화났나 싶어서 불안하고 초조해져요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"인간관계"
    }
  },
  {
    "content":"새로운 환경에서 친구를 사귈 수 있을지 걱정되고 위축돼요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"인간관계"
    }
  },
  {
    "content":"가족에게 나쁜 소식을 전해야 할 때 어떻게 말할지 고민돼요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"인간관계"
    }
  },
  {
    "content":"사과해야 할 상황에서 거절당할까 봐 용기를 내지 못하고 있어요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"인간관계"
    }
  },
  {
    "content":"중요한 사람의 기분을 상하게 했을까 봐 계속 확인하고 싶어져요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"인간관계"
    }
  },
  {
    "content":"중요한 시험 당일이 다가올수록 잠을 설치며 긴장이 고조돼요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"결혼식이나 돌잔치 같은 행사 준비로 실수할까 봐 불안해요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"면접 날짜가 정해지고 나서 준비가 충분할지 걱정되고 초조해요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"이사 날짜가 임박하면서 준비 과정에서 문제가 생길까 봐 긴장돼요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"가족 여행을 앞두고 계획대로 진행될지 걱정이 많아져요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"첫 출근일이 다가오면서 새로운 환경에 적응할 수 있을지 불안해요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"중요한 발표나 공연을 앞두고 실수할까 봐 며칠 전부터 떨려요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"생일파티나 기념일 준비가 만족스럽지 않을까 봐 스트레스받아요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"운전면허나 자격증 시험 전날에는 항상 잠이 오지 않아요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"새학기나 새 직장 시작 전에 준비가 부족한 것 같아서 불안해요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"병원 검사나 시술 날짜가 다가오면 결과가 걱정되어 긴장돼요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"중요한 미팅이나 상담 전에 어떤 질문을 받을지 몰라서 초조해요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"여행 출발일이 가까워지면 챙겨야 할 것들 때문에 마음이 급해져요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"집들이나 파티를 열기 전에 준비가 완벽하지 않을까 봐 걱정돼요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"중요한 계약이나 서명일을 앞두고 조건을 제대로 검토했는지 불안해요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"혼자 있을 때 부정적인 생각들이 계속 떠올라서 마음이 불안해요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"미래에 대한 막연한 걱정 때문에 현재에 집중하기 어려워요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"완벽해야 한다는 압박감 때문에 작은 실수에도 과도하게 긴장해요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"다른 사람들의 평가가 신경 쓰여서 자연스럽게 행동하기 어려워요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"감정을 제대로 표현하지 못할까 봐 대화할 때마다 위축돼요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"결정을 내려야 할 때마다 잘못된 선택을 할까 봐 고민만 계속해요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"과거의 실수가 다시 반복될까 봐 새로운 시도를 하기 전에 망설여요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"타인과 비교하는 습관 때문에 자존감이 떨어지고 불안해져요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"갑작스런 감정 변화가 올까 봐 스스로를 계속 모니터링하게 돼요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"중요한 순간에 실수할까 봐 미리부터 온갖 시나리오를 생각해요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"마음의 평정을 유지하지 못할까 봐 명상이나 휴식도 긴장되어 해요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"스트레스를 제대로 관리하지 못할까 봐 오히려 더 스트레스받아요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"내 감정이 다른 사람에게 부담이 될까 봐 솔직하게 표현하지 못해요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"심리적 안정감을 찾지 못할까 봐 작은 변화에도 민감하게 반응해요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"정신적 성장이 멈춘 것 같아서 현재 상태에 대한 불안감이 커져요.",
    "metadata":{
      "emotion":"불안과 긴장",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"요리를 실패해서 음식을 버리게 되어 자원 낭비한 것 같아 자책돼요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"친구들과의 약속에 늦어서 민폐를 끼친 것 같아 부끄럽고 미안해요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"집안 정리를 제대로 못해서 방문객 앞에서 창피하고 부끄러웠어요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"운동을 시작했다가 작심삼일로 끝나서 의지가 약한 나 자신이 한심해요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"쇼핑에서 충동구매를 하고 나서 자제력 없는 내가 부끄럽고 후회돼요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"반려동물을 제대로 돌보지 못한 것 같아서 자책감에 시달리고 있어요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"취미 활동에서 실력이 늘지 않아서 재능 없는 내가 부끄럽게 느껴져요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"가족과의 시간을 소홀히 한 것 같아서 죄책감이 들고 미안해요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"독서 목표를 달성하지 못해서 게으른 나 자신을 자책하고 있어요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"여행에서 계획을 제대로 세우지 못해 일행에게 피해를 준 것 같아 미안해요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"집 주변 이웃에게 소음 피해를 줬을까 봐 부끄럽고 죄송한 마음이에요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"건강 관리를 소홀히 해서 몸이 안 좋아진 게 내 탓인 것 같아 자책돼요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"좋은 습관을 만들려고 했다가 실패해서 나약한 내가 한심하게 느껴져요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"여가 시간을 의미 없이 보낸 것 같아서 시간을 낭비한 것이 부끄러워요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"다른 사람들보다 일상을 잘 관리하지 못하는 내가 부족하게 느껴져요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"건강 관리를 소홀히 해서 병이 생긴 것이 내 잘못인 것 같아 자책돼요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"의사의 조언을 따르지 않아서 증상이 악화된 것 같아 후회하고 있어요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"규칙적인 운동을 하지 못해서 체력이 떨어진 것이 부끄럽고 한심해요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"스트레스 관리를 제대로 못해서 몸이 망가진 것 같아 자책감이 들어요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"금연이나 금주에 실패해서 의지력 없는 내가 부끄럽고 실망스러워요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"가족에게 건강상 걱정을 끼친 것 같아서 죄책감이 들고 미안해요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"정기 검진을 미뤄서 조기 발견 기회를 놓친 것 같아 자책하고 있어요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"식단 관리를 제대로 하지 못해서 건강이 나빠진 것이 내 탓 같아요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"수면 패턴을 지키지 못해서 컨디션이 안 좋아진 것을 자책하고 있어요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"건강보험료를 제때 내지 못해서 혜택을 받지 못한 것이 부끄러워요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"정신건강 관리를 소홀히 해서 우울해진 것이 내 잘못인 것 같아요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"몸의 이상 신호를 무시한 것이 무책임했다는 생각에 자책돼요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"가족력이 있는 질병 예방을 위한 노력을 안 한 것이 부끄럽고 후회돼요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"약물 복용을 잊어버려서 치료에 소홀한 것 같아 죄책감이 들어요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"건강한 생활습관을 만들지 못한 게 게으른 내 탓인 것 같아 한심해요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"SNS에 부적절한 글을 올려서 이미지를 망친 것 같아 부끄럽고 후회돼요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"온라인에서 타인과 논쟁하며 감정적으로 반응한 것이 성숙하지 못한 것 같아 창피해요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"디지털 기기 조작 미숙으로 중요한 파일을 삭제한 것이 무능한 내 탓 같아서 자책돼요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"온라인 쇼핑 중독으로 과소비한 것이 자제력 없는 내 모습 같아서 부끄러워요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"화상회의에서 기술적 실수로 회의를 방해한 것이 준비 부족한 내 탓 같아 미안해요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"개인정보를 제대로 관리하지 못해서 유출 위험에 노출된 것이 부주의한 내 잘못이에요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"온라인 게임에 과몰입해서 시간을 낭비한 것이 의지력 없는 내가 한심해요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"가짜 뉴스를 확인 없이 공유해서 정보 오염에 기여한 것이 부끄럽고 자책돼요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"디지털 리터러시 부족으로 사기에 당한 것이 무지한 내 탓인 것 같아요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"온라인에서 무례한 댓글을 단 것이 예의 없는 내 모습 같아서 창피해요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"중요한 이메일을 놓쳐서 업무에 차질을 빚은 것이 무책임한 내 탓 같아 자책돼요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"소셜미디어 중독으로 실제 관계를 소홀히 한 것이 본말전도인 것 같아 부끄러워요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"온라인 강의를 제대로 듣지 않아서 돈을 낭비한 것이 게으른 내 탓 같아요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"디지털 기기에 의존해서 기본적인 능력을 잃은 것 같아서 퇴보한 내가 한심해요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"온라인에서 익명성에 숨어 부적절한 행동을 한 것이 비겁한 내 모습 같아서 창피해요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"중요한 업무에서 실수를 해서 팀에 피해를 준 것 같아 자책감이 커요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"회의에서 준비 부족으로 제대로 발언하지 못해 부끄럽고 후회돼요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"동료들보다 업무 속도가 느려서 능력 부족한 내가 부끄럽게 느껴져요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"상사의 기대에 못 미치는 결과를 내서 실망시킨 것 같아 죄송해요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"마감을 놓쳐서 다른 사람들에게 피해를 준 것에 대해 자책하고 있어요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"새로운 기술을 배우는 속도가 느려서 뒤처지는 내가 한심해요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"시험에서 좋지 않은 결과를 받아서 노력하지 않은 내가 부끄러워요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"프레젠테이션에서 버벅거려서 청중들 앞에서 창피하고 모욕감을 느꼈어요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"업무 관련 교육에서 이해하지 못해 질문도 못하고 부끄러웠어요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"동료의 도움을 받고도 제대로 성과를 내지 못해서 미안하고 자책돼요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"중요한 업무를 잊어버려서 무책임한 내가 부끄럽고 죄책감이 들어요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"학습 목표를 달성하지 못해서 게으른 나 자신이 한심하게 느껴져요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"경력에 비해 실력이 부족한 것 같아서 동료들 앞에서 위축되고 부끄러워요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"업무상 갈등을 잘 해결하지 못해서 성숙하지 못한 내가 창피해요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"승진 기회를 놓친 것이 내 부족함 때문인 것 같아서 자책하고 있어요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"가계 관리를 제대로 못해서 경제적 어려움을 자초한 것 같아 자책돼요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"투자 실패로 손실을 본 것이 공부 부족한 내 탓인 것 같아 부끄러워요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"충동구매로 예산을 초과한 것이 자제력 없는 내 모습 같아서 한심해요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"가족의 경제적 부담을 덜어주지 못해서 무능한 내가 부끄럽고 미안해요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"적금을 중도 해지해야 하는 상황이 계획성 없는 내 탓 같아서 자책돼요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"신용카드 연체로 신용등급이 떨어진 것이 무책임한 내 잘못인 것 같아요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"보험 가입을 미뤄서 보장받지 못한 것이 미련한 선택이었다고 후회해요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"사기에 당해서 돈을 잃은 것이 판단력 부족한 내 탓인 것 같아 부끄러워요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"노후 준비를 하지 않은 것이 미래를 생각 안 한 내 잘못 같아서 자책돼요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"용돈 관리를 못해서 부모님께 손 벌린 것이 부끄럽고 죄송해요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"경제적 여유가 없어서 친구들과 어울리지 못하는 내가 초라하게 느껴져요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"투자 공부를 게을리 해서 기회를 놓친 것이 나태한 내 탓 같아요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"물가 상승에 대비하지 못한 것이 무계획한 내 모습 같아서 한심해요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"가족 경조사비를 준비하지 못해서 체면을 구긴 것이 부끄러워요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"세금 신고를 제대로 하지 못해서 불이익을 받은 것이 무지한 내 탓 같아요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"부정적인 생각만 하는 내가 정신적으로 약한 것 같아서 부끄럽고 자책돼요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"감정 조절을 못해서 주변 사람들을 힘들게 한 것이 미성숙한 내 탓 같아요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"자존감이 낮아서 스스로를 사랑하지 못하는 내가 한심하게 느껴져요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"완벽주의 성향 때문에 스스로를 괴롭히는 것이 어리석은 내 모습 같아서 자책돼요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"질투심이나 시기심을 느끼는 내가 인격적으로 부족한 것 같아서 부끄러워요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"우울감을 극복하지 못하는 것이 의지력 부족한 내 탓인 것 같아서 자책돼요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"분노를 표출한 후 후회하는 것이 감정 관리 능력 없는 내 모습 같아 창피해요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"과거에 얽매여서 앞으로 나아가지 못하는 내가 발전성 없는 것 같아 한심해요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"타인과 비교하며 열등감을 느끼는 것이 자신감 없는 내 모습 같아서 부끄러워요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"스트레스를 건강하게 해소하지 못하는 것이 미숙한 내 탓 같아서 자책돼요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"자기 혐오에 빠져서 건설적이지 못한 내가 정신적으로 약한 것 같아 부끄러워요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"결정 장애로 기회를 놓치는 것이 우유부단한 내 성격 탓인 것 같아서 한심해요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"내면의 갈등을 해결하지 못하는 것이 성숙하지 못한 내 모습 같아서 자책돼요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"부정적인 감정에 휩쓸리는 것이 정신력 부족한 내 탓인 것 같아서 창피해요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"자아성찰을 게을리 해서 성장하지 못하는 것이 나태한 내 모습 같아서 부끄러워요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"친구와의 갈등에서 먼저 사과하지 못한 내가 고집스럽고 부끄러워요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"인간관계"
    }
  },
  {
    "content":"가족에게 화를 내고 나서 감정 조절 못한 내가 한심하고 죄책감이 들어요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"인간관계"
    }
  },
  {
    "content":"다른 사람의 비밀을 실수로 말해버려서 신뢰를 깬 것 같아 자책돼요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"인간관계"
    }
  },
  {
    "content":"연인과의 관계에서 이기적으로 행동한 것 같아서 미안하고 부끄러워요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"인간관계"
    }
  },
  {
    "content":"친구의 어려운 상황을 외면한 것 같아서 냉정한 내가 부끄럽게 느껴져요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"인간관계"
    }
  },
  {
    "content":"사회적 모임에서 적절하지 못한 발언을 해서 분위기를 망친 것 같아 창피해요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"인간관계"
    }
  },
  {
    "content":"다른 사람을 무의식적으로 상처입힌 것 같아서 배려심 없는 내가 부끄러워요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"인간관계"
    }
  },
  {
    "content":"가족의 기대에 부응하지 못해서 실망시킨 것 같아 죄책감이 들어요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"인간관계"
    }
  },
  {
    "content":"친구들 사이에서 질투심을 드러낸 것 같아서 성격이 나쁜 내가 창피해요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"인간관계"
    }
  },
  {
    "content":"중요한 사람의 연락을 무시한 것 같아서 무례한 내가 부끄럽고 미안해요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"인간관계"
    }
  },
  {
    "content":"대화에서 상대방의 말을 제대로 들어주지 못해서 자기중심적인 내가 한심해요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"인간관계"
    }
  },
  {
    "content":"다른 사람과 비교하며 불평한 것이 부정적인 내 모습 같아서 부끄러워요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"인간관계"
    }
  },
  {
    "content":"도움을 요청받았을 때 거절한 것이 이기적이었나 싶어서 자책돼요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"인간관계"
    }
  },
  {
    "content":"인간관계에서 진심을 보이지 못한 것 같아서 소극적인 내가 부끄러워요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"인간관계"
    }
  },
  {
    "content":"가족이나 친구의 조언을 무시한 것이 고마움을 모르는 태도 같아서 미안해요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"인간관계"
    }
  },
  {
    "content":"중요한 시험에서 실패해서 기대에 부응하지 못한 것이 부끄럽고 자책돼요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"결혼식 준비를 제대로 못해서 하객들에게 민폐를 끼친 것 같아 미안해요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"졸업식에서 성적이 좋지 않아서 부모님께 창피를 드린 것 같아 죄송해요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"면접에서 떨어진 것이 준비 부족한 내 탓인 것 같아서 자책하고 있어요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"생일파티를 망쳐서 친구들을 실망시킨 것 같아 부끄럽고 미안해요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"가족 행사에서 실수해서 분위기를 어색하게 만든 것이 창피하고 후회돼요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"첫 출근일에 늦어서 첫인상을 망친 것이 무책임한 내 모습 같아서 부끄러워요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"중요한 발표회에서 실패해서 기대했던 사람들을 실망시킨 것 같아 자책돼요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"이사 과정에서 분실 사고가 나서 가족에게 피해를 준 것이 죄책감 들어요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"여행에서 계획을 잘못 세워서 일행에게 불편을 끼친 것이 미안하고 부끄러워요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"운전면허 시험에 계속 떨어져서 무능한 내가 창피하고 한심하게 느껴져요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"새해 결심을 지키지 못해서 의지력 없는 내가 부끄럽고 자책돼요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"기념일을 깜빡해서 소중한 사람을 서운하게 한 것이 무성의한 것 같아 미안해요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"입학식에서 준비 부족으로 어색한 상황을 만든 것이 부끄럽고 후회돼요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"퇴직식에서 감정 조절을 못해서 동료들 앞에서 창피한 모습을 보인 것 같아요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"창작 목표를 달성하지 못해서 의지력 없는 내가 부끄럽고 자책돼요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"다른 창작자들과 비교해서 실력이 부족한 내가 재능 없는 것 같아서 한심해요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"작품에 대한 혹평을 받고 나서 실력 부족한 내가 창피하고 위축돼요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"창작 과정에서 포기한 것이 끈기 없는 내 성격 탓인 것 같아서 자책돼요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"영감 부족으로 작품을 완성하지 못한 것이 노력 부족한 내 탓 같아서 부끄러워요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"새로운 기술 습득에 실패해서 학습 능력 부족한 내가 한계가 있는 것 같아요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"창작 활동을 꾸준히 하지 못한 것이 게으른 내 모습 같아서 자책하고 있어요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"작품의 완성도가 낮아서 실력 향상이 없는 내가 발전성 없는 것 같아 부끄러워요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"창작 과정에서 슬럼프를 극복하지 못한 것이 정신력 부족한 내 탓 같아요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"비판을 수용하지 못하고 감정적으로 반응한 것이 미성숙한 내 모습 같아서 창피해요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"창작물에 대한 자신감 부족으로 공개하지 못한 것이 소극적인 내 성격 탓 같아요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"새로운 장르에 도전하지 못하는 것이 용기 없는 내 모습 같아서 한심해요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"창작 활동에 충분한 시간을 투자하지 못한 것이 우선순위를 잘못 정한 내 탓이에요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"다른 사람의 작품을 보고 질투심을 느낀 것이 인격적으로 부족한 내 모습 같아서 부끄러워요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"성장 속도가 느린 것이 노력 부족한 내 탓인 것 같아서 자책감이 들어요.",
    "metadata":{
      "emotion":"수치와 자책",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"혼자 보내는 주말이 길고 공허해서 세상과 단절된 기분이 들어요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"좋아하던 취미를 더 이상 즐기지 못하게 되어서 일부분을 잃은 것 같아요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"반려동물을 떠나보내고 나서 집안이 너무 조용하고 적막해요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"동네에서 오래 살았던 단골 가게가 문을 닫아서 추억의 공간을 잃은 기분이에요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"친구들이 모두 각자 바빠져서 함께할 사람이 없어 외롭고 소외감을 느껴요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"즐겨 보던 TV 프로그램이 종영되어서 일상의 소소한 즐거움을 잃었어요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"코로나로 인해 예전처럼 자유롭게 여행을 갈 수 없어서 활력을 잃은 기분이에요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"오랫동안 다니던 동호회에서 나오게 되어서 소속감을 잃고 허전해요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"건강 문제로 좋아하던 운동을 그만두게 되어서 정체성의 일부를 잃은 것 같아요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"가족들과 함께 보내던 시간이 줄어들어서 유대감이 약해진 것 같아 서운해요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"이사로 인해 오랫동안 정들었던 동네를 떠나게 되어서 뿌리를 잃은 기분이에요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"나이가 들면서 체력이 떨어져 예전에 즐기던 활동들을 포기하게 되어 아쉬워요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"경제적 어려움으로 여가 활동을 줄이게 되어서 삶의 재미를 잃은 것 같아요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"혼자 밥을 먹는 시간이 늘어나면서 식사마저 쓸쓸하고 무미건조해졌어요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"새로운 환경에 적응하지 못해서 예전 생활에 대한 그리움과 상실감이 커요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"만성 질환 진단을 받고 나서 건강한 삶에 대한 자신감과 미래를 잃은 것 같아요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"수술로 인해 신체 일부를 잃게 되어서 완전한 내가 아닌 것 같은 상실감이 들어요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"나이가 들면서 시력이나 청력이 떨어져서 세상과의 연결고리를 잃어가는 기분이에요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"정신건강 문제로 인해 예전의 활기찬 모습을 잃고 무기력한 상태가 지속돼요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"의료진과의 소통이 어려워서 치료 과정에서 소외되고 혼자 감당해야 하는 기분이에요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"장기간 입원으로 인해 일상생활과 사회적 관계에서 멀어져서 고립감을 느껴요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"가족의 건강 악화를 지켜보면서 예전의 그 사람을 점점 잃어가는 슬픔이 커요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"치료 부작용으로 인해 예전의 체력과 활력을 잃어서 삶의 질이 떨어진 기분이에요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"희귀 질환으로 인해 다른 사람들이 이해하지 못하는 고통 속에서 혼자 있는 기분이에요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"의료비 부담으로 치료를 포기하게 되어서 건강 회복의 기회를 상실한 것 같아요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"운동 능력을 잃게 되어서 스포츠나 신체 활동을 통한 즐거움을 포기해야 해요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"기억력 저하로 인해 소중한 추억들을 잃어가는 것 같아서 정체성까지 흔들려요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"만성 통증으로 인해 정상적인 생활이 불가능해져서 삶의 의욕을 잃었어요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"건강 검진에서 나쁜 결과를 받고 미래에 대한 희망과 계획을 잃은 기분이에요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"치료 과정에서 의료진의 무관심으로 인간적 돌봄을 받지 못하는 소외감을 느껴요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"소셜미디어에서 친구들의 활발한 소통을 보면서 혼자만 소외된 것 같은 기분이 들어요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"온라인 커뮤니티에서 추방당해서 유일한 소통 창구와 소속감을 잃은 것 같아요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"디지털 기기 조작 미숙으로 온라인 활동에서 소외되고 시대에 뒤처진 기분이에요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"해킹으로 인해 디지털 자산과 개인 정보를 모두 잃어서 온라인 정체성까지 상실했어요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"온라인 친구들과의 연락이 끊기면서 디지털 세상에서도 혼자가 된 기분이에요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"플랫폼 변화로 오랫동안 운영했던 블로그나 채널을 잃어서 표현 공간을 상실했어요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"인터넷 연결이 불안정해서 온라인 세상과 단절되고 정보에서 소외되는 느낌이에요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"온라인 게임에서 계정이 삭제되어서 오랫동안 쌓아온 성과와 추억을 모두 잃었어요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"가짜 뉴스나 사기로 인해 온라인에 대한 신뢰를 잃고 디지털 세상이 두려워졌어요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"세대 차이로 인해 새로운 디지털 트렌드를 따라가지 못해서 소외감을 느껴요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"온라인 쇼핑몰이나 서비스가 종료되어서 익숙했던 디지털 생활 패턴을 잃었어요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"사이버 괴롭힘으로 인해 온라인 활동을 중단하게 되어서 표현의 자유를 잃은 기분이에요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"디지털 격차로 인해 정보 접근에서 소외되고 사회 참여 기회를 놓치는 것 같아요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"온라인 강의나 회의에서 기술적 문제로 참여하지 못해서 학습이나 업무 기회를 잃었어요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"클라우드 서비스 오류로 중요한 디지털 자료들을 잃어서 디지털 기억을 상실한 기분이에요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"팀에서 중요한 프로젝트에서 제외되어서 동료들로부터 소외된 기분이 들어요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"오랫동안 근무했던 회사를 퇴사하게 되어서 직업적 정체성을 잃은 것 같아요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"승진에서 누락되어서 인정받지 못하는 느낌과 함께 기회를 상실한 것 같아요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"새로운 업무 환경에서 적응하지 못해 예전 직장에 대한 그리움이 커져요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"동료들과의 관계가 소원해져서 직장 내에서 혼자 있는 시간이 많아졌어요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"자동화로 인해 내 업무가 사라질까 봐 직업적 존재 의미를 잃을 것 같아 불안해요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"학업을 중단하게 되어서 학문적 목표와 꿈을 포기한 것 같아 허무해요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"은퇴 후 직장 동료들과의 연락이 끊기면서 사회적 관계를 잃은 기분이에요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"전공과 다른 분야에서 일하게 되어서 전문성을 잃어가는 것 같아 아쉬워요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"리모트 워크로 인해 동료들과의 소통이 줄어들어서 소속감을 잃었어요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"중요한 업무에서 실패한 후 상사의 신뢰를 잃은 것 같아서 위치가 애매해졌어요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"회사 구조조정으로 팀이 해체되어서 오랫동안 쌓아온 유대감을 잃었어요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"새로운 기술을 따라가지 못해서 업무에서 뒤처지는 느낌과 소외감이 들어요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"멘토나 롤모델이었던 선배가 퇴사해서 의지할 곳을 잃은 기분이에요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"학습 동기를 잃어버려서 성장에 대한 열정과 목표 의식이 사라진 것 같아요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"실직으로 인해 경제적 안정과 함께 사회적 지위까지 잃은 것 같아서 무력감이 들어요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"투자 실패로 평생 모은 돈을 잃어서 미래에 대한 계획과 꿈까지 포기해야 할 것 같아요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"경제적 어려움으로 친구들과의 모임에 참여하지 못해서 사회적 관계마저 잃어가요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"집을 잃게 되어서 안정감과 소속감, 그리고 추억이 담긴 공간을 모두 상실했어요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"신용불량자가 되어서 사회적 신뢰와 함께 자존감까지 잃은 것 같아 위축돼요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"사기를 당해서 돈뿐만 아니라 사람에 대한 신뢰까지 잃어버린 기분이에요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"노후 준비금을 잃어서 안정적인 미래에 대한 희망과 기대를 포기해야 할 것 같아요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"가족의 경제적 문제로 인해 화목했던 관계마저 소원해져서 이중의 상실감을 느껴요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"물가 상승으로 예전처럼 생활할 수 없어서 삶의 질과 여유를 잃은 것 같아요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"경기 침체로 사업이 망해서 오랫동안 쌓아온 것들을 모두 잃게 되어 절망스러워요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"금융 상품의 손실로 인해 자녀 교육비를 마련하지 못해서 꿈마저 포기해야 할 것 같아요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"경제적 격차로 인해 사회에서 소외되고 계층 이동의 기회를 잃은 것 같아요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"보험 보장을 받지 못해서 의료비 부담으로 치료 기회까지 상실하게 되었어요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"은퇴 후 수입 감소로 사회적 활동이 제한되어서 인간관계마저 잃어가는 기분이에요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"부채 상환으로 인해 여유 있던 생활을 포기하고 최소한의 생활만 유지하게 되어 우울해요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"우울감이 깊어지면서 예전의 밝고 긍정적이었던 내 모습을 잃어가는 것 같아요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"자신감을 잃어버려서 도전하고 성장하려는 의욕까지 상실한 것 같아 무기력해요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"삶의 목적과 의미를 찾지 못해서 방향감각을 잃고 표류하는 기분이에요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"감정을 느끼는 능력이 둔해져서 기쁨이나 슬픔 같은 생생한 감정을 잃은 것 같아요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"과거의 트라우마로 인해 순수했던 마음과 타인에 대한 신뢰를 잃어버렸어요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"완벽주의에 매몰되어서 자연스럽고 편안한 내 모습을 잃고 경직되어 가는 것 같아요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"스트레스가 누적되어서 마음의 평정과 내적 안정감을 상실한 기분이에요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"자아 정체성에 대한 혼란으로 진정한 나 자신을 잃어버린 것 같아서 막막해요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"희망을 잃어버려서 미래에 대한 기대와 꿈을 포기하게 된 것 같아 절망스러워요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"감정 조절 능력을 잃어서 예전처럼 균형 잡힌 상태를 유지하지 못하고 있어요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"창의성과 상상력이 메말라서 풍부했던 내면의 세계를 잃어가는 기분이에요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"자기 사랑과 자존감을 잃어서 스스로를 돌보고 아끼는 마음까지 사라졌어요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"영적인 연결감을 잃어서 삶의 신성함과 경외감을 느끼지 못하게 되었어요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"내면의 목소리를 잃어서 직감이나 내적 지혜에 의존하지 못하고 혼란스러워요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"감사하는 마음을 잃어서 일상의 소소한 기쁨과 행복을 느끼지 못하게 되었어요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"가까웠던 친구가 연락을 끊으면서 소중한 인연을 잃은 것 같아 서운하고 외로워요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"인간관계"
    }
  },
  {
    "content":"연인과 헤어진 후 그 사람과 공유했던 모든 추억과 미래 계획을 잃은 기분이에요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"인간관계"
    }
  },
  {
    "content":"가족 간의 갈등으로 예전처럼 가까워지지 못해서 유대감을 상실한 것 같아요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"인간관계"
    }
  },
  {
    "content":"친구들의 결혼과 육아로 만날 기회가 줄어들어서 우정이 소원해진 것 같아 아쉬워요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"인간관계"
    }
  },
  {
    "content":"이사나 이직으로 인해 오랫동안 만나던 사람들과 거리가 멀어져서 인맥을 잃었어요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"인간관계"
    }
  },
  {
    "content":"SNS에서 친구에게 차단당해서 관계의 단절감과 거부감을 느끼고 있어요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"인간관계"
    }
  },
  {
    "content":"소중한 사람의 갑작스런 죽음으로 영원히 만날 수 없게 되어서 깊은 상실감에 빠졌어요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"인간관계"
    }
  },
  {
    "content":"그룹 내에서 따돌림을 당해서 소속감을 잃고 혼자 남겨진 기분이에요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"인간관계"
    }
  },
  {
    "content":"오해로 인해 오랜 친구와 관계가 틀어져서 신뢰와 우정을 잃은 것 같아 허무해요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"인간관계"
    }
  },
  {
    "content":"가족의 이민이나 원거리 이주로 물리적 거리감과 함께 감정적 거리도 멀어져요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"인간관계"
    }
  },
  {
    "content":"동창들과의 모임에서 소외되어서 학창시절 추억까지 빛이 바랜 것 같아요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"인간관계"
    }
  },
  {
    "content":"멘토나 조언자 역할을 해주던 어르신을 잃어서 인생의 나침반을 상실한 기분이에요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"인간관계"
    }
  },
  {
    "content":"온라인으로만 만나게 되면서 예전의 깊은 유대감과 친밀감을 잃은 것 같아요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"인간관계"
    }
  },
  {
    "content":"새로운 환경에서 친구를 사귀지 못해서 사회적 연결망을 잃고 고립된 기분이에요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"인간관계"
    }
  },
  {
    "content":"세대 차이로 인해 젊은 사람들과 소통이 어려워져서 시대와 동떨어진 느낌이 들어요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"인간관계"
    }
  },
  {
    "content":"중요한 시험에 떨어져서 오랫동안 준비했던 꿈과 목표를 잃은 것 같아 허무해요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"결혼식에서 가족의 부재로 완전한 축복을 받지 못한 것 같아서 아쉽고 서운해요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"졸업과 함께 학교라는 소속감과 친구들과의 일상적 만남을 잃게 되어 섭섭해요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"이별로 인해 연인과 계획했던 모든 미래와 함께할 시간들을 상실하게 되어 슬퍼요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"가족의 부고 소식으로 더 이상 대화할 수 없게 되어서 깊은 상실감에 잠겨요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"첫 직장을 그만두면서 사회 초년생으로서의 설렘과 기대를 잃은 것 같아요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"이사로 인해 오랫동안 정들었던 이웃들과 지역 커뮤니티를 떠나게 되어 외로워요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"중요한 기회를 놓쳐서 인생의 전환점이 될 수 있었던 순간을 잃어버린 기분이에요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"새해를 혼자 맞이하게 되어서 함께 축하할 사람들과의 연대감을 잃은 것 같아요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"은퇴식에서 직장 생활의 마무리와 함께 역할과 정체성을 상실한 기분이에요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"생일을 조용히 보내면서 예전처럼 축하받는 특별함을 잃은 것 같아 쓸쓸해요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"입학 실패로 인해 새로운 환경에서의 성장 기회를 놓친 것 같아서 좌절스러워요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"여행 계획이 취소되면서 새로운 경험과 추억을 만들 기회를 잃어서 아쉬워요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"중요한 사람의 결혼식에 참석하지 못해서 소중한 순간을 함께하지 못한 것이 서운해요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"오랫동안 기다린 공연이나 행사가 취소되어서 기대했던 특별한 경험을 잃었어요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"창작 영감을 잃어버려서 예전처럼 자유롭고 창의적인 표현을 하지 못하게 되었어요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"창작 동료들과의 관계가 소원해져서 함께 성장하고 격려받던 환경을 잃었어요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"슬럼프에 빠져서 작품에 대한 자신감과 창작 의욕을 모두 상실한 것 같아요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"창작 활동을 중단하게 되어서 예술가로서의 정체성과 목적의식을 잃은 기분이에요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"새로운 기술을 따라가지 못해서 창작 분야에서 소외되고 뒤처지는 느낌이 들어요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"창작물에 대한 혹평으로 인해 표현에 대한 용기와 자유로움을 잃어버렸어요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"창작 지원이나 기회를 얻지 못해서 꿈을 포기하고 현실에 안주해야 할 것 같아요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"상업적 성공에 실패해서 창작 활동을 지속할 경제적 기반을 잃게 되었어요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"원래 스타일을 잃어버려서 자신만의 독창적인 목소리를 찾지 못하고 있어요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"창작 커뮤니티에서 배제되어서 피드백과 성장의 기회를 상실한 것 같아요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"기술적 한계에 부딪혀서 표현하고 싶은 것을 구현할 능력을 잃은 것 같아 좌절스러워요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"창작에 대한 열정을 잃어서 예전처럼 몰입하고 즐거워하는 마음이 사라졌어요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"멘토나 스승을 잃어서 창작 여정에서 방향을 제시받을 수 있는 길잡이를 상실했어요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"창작 시간을 확보하지 못해서 지속적인 성장과 발전의 기회를 놓치고 있어요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"비교와 경쟁에 지쳐서 순수한 창작 동기와 예술에 대한 사랑을 잃어가는 것 같아요.",
    "metadata":{
      "emotion":"소외와 상실",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"어린 시절 여름휴가 때의 자유롭고 걱정 없던 시간들이 그립고 아련해요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"코로나 이전의 자유로운 여행과 나들이가 가능했던 때가 그리워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"가족과 함께 보냈던 평범한 저녁 시간들이 지금은 소중하게 느껴져서 그리워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"학창시절 친구들과 함께했던 무의미하지만 즐거웠던 시간들이 아쉽고 그리워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"이사 전 살던 동네의 익숙한 풍경과 단골 가게들이 그립고 아쉬워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"반려동물과 함께 산책했던 평화로운 일상이 지금은 소중한 추억으로만 남아서 그리워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"젊었을 때의 체력과 활력으로 자유롭게 운동하던 시절이 아쉽고 그리워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"시간적 여유가 있어서 취미에 푹 빠져 지낼 수 있었던 때가 그립고 부러워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"가족 모두가 건강하고 화목했던 평범한 일상이 얼마나 소중했는지 새삼 그리워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"좋아하던 카페나 식당이 문을 닫아서 그곳에서의 추억들이 아쉽고 그리워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"계절의 변화를 여유롭게 느끼며 산책할 수 있었던 한가한 시간들이 그리워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"스마트폰 없이도 충분히 행복했던 단순하고 순수한 여가 시간이 그리워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"친구들과 밤새 게임하고 수다떨며 시간 가는 줄 모르던 대학 시절이 그리워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"경제적 걱정 없이 하고 싶은 취미 활동을 마음껏 할 수 있었던 때가 아쉬워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"주말마다 새로운 곳을 탐험하고 모험을 즐겼던 활기찬 시절이 그립고 아쉬워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"아프지 않고 건강했을 때의 활기찬 몸과 자유로운 일상이 그립고 소중했어요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"밤새도록 놀아도 다음날 멀쩡했던 젊은 시절의 체력과 회복력이 그리워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"건강 걱정 없이 마음껏 먹고 싶은 음식을 즐길 수 있었던 때가 그립고 아쉬워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"운동을 즐겁게 하며 몸의 변화를 실감했던 건강한 시절이 그리워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"가족 모두가 건강해서 병원 갈 일이 없었던 평범하고 소중한 일상이 그리워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"수면의 질이 좋아서 깊게 잠들고 개운하게 일어났던 시절이 그립고 부러워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"스트레스 없이 마음이 편안하고 정신적으로 안정되어 있던 때가 그리워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"시력이 좋아서 안경 없이도 선명하게 세상을 볼 수 있었던 시절이 아쉽고 그리워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"약물에 의존하지 않고도 자연스럽게 건강을 유지했던 시절이 그립고 소중해요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"몸이 가벼워서 계단을 뛰어 올라가도 힘들지 않았던 때가 그리워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"병원 가는 것이 예방 차원이었지 치료 목적이 아니었던 건강한 시절이 그리워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"면역력이 강해서 감기도 잘 걸리지 않았던 튼튼한 몸이 그립고 아쉬워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"건강한 가족과 함께 활동적인 여행이나 운동을 즐겼던 시간들이 그리워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"정신적으로 맑고 집중력이 좋아서 머리가 명쾌했던 컨디션이 그리워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"아무 걱정 없이 미래를 계획할 수 있을 만큼 건강에 자신이 있었던 때가 그리워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"인터넷이 없던 시절의 단순하고 집중력 있는 생활이 그립고 부러워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"스마트폰 없이도 충분히 행복했던 직접적이고 진정한 소통의 시절이 그리워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"온라인 게임을 처음 시작했을 때의 신선한 재미와 몰입감이 그립고 아쉬워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"SNS가 순수하게 친구들과 소통하는 공간이었던 초기의 따뜻함이 그리워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"디지털 기기 없이도 책이나 자연과 깊이 교감할 수 있었던 시절이 그리워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"온라인 커뮤니티에서 진심으로 소통하고 도움을 주고받던 훈훈한 문화가 그리워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"사진을 필름으로 찍어서 현상할 때까지 기다리던 설렘과 소중함이 그리워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"이메일이 특별한 소통 수단이었고 편지 쓰는 마음으로 정성스럽게 썼던 때가 그리워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"온라인 쇼핑이 새롭고 신기했던 시절의 호기심과 기대감이 그립고 아쉬워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"인터넷 속도가 느려도 기다리는 것이 당연했던 여유로운 디지털 문화가 그리워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"온라인에서 만난 사람들과 순수하게 우정을 나눴던 초기 인터넷 문화가 그리워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"디지털 기기가 단순해서 조작이 쉽고 고장도 적었던 시절이 그립고 아쉬워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"온라인과 오프라인의 경계가 명확해서 휴식할 수 있었던 시절이 그리워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"개인정보 걱정 없이 자유롭게 온라인 활동을 즐겼던 때가 그립고 부러워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"디지털 기술의 발전이 희망적이고 긍정적으로만 느껴졌던 순수한 시절이 그리워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"첫 직장에서 느꼈던 설렘과 열정, 모든 것이 새로웠던 그 시절이 그리워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"동료들과 함께 야근하면서도 즐거웠던 팀워크와 유대감이 아쉽고 그리워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"학창시절 시험 공부는 힘들었지만 목표가 명확했던 단순한 시절이 그리워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"멘토였던 선배나 상사와 함께 일하며 배우고 성장했던 시간들이 그립고 소중해요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"승진이나 성취에 대한 순수한 기쁨과 성취감을 느꼈던 초심이 그리워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"새로운 것을 배우는 것이 즐겁고 호기심으로 가득했던 학습에 대한 열정이 그리워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"회사 동료들과 퇴근 후 함께 어울리며 나눴던 진솔한 대화들이 그립고 아쉬워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"실패를 두려워하지 않고 도전했던 용기와 패기가 있었던 시절이 그리워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"업무 스트레스 없이 순수하게 학문에만 몰입할 수 있었던 대학원 시절이 그리워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"작은 성과에도 크게 기뻐하고 격려받았던 신입사원 때의 순수함이 그립고 아쉬워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"야망과 꿈으로 가득했던 커리어 초기의 열정과 에너지가 그리워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"동기들과 함께 고민하고 성장해나갔던 동반자적 관계가 아쉽고 그리워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"매일이 배움의 연속이었던 인턴십이나 수습 기간의 신선함이 그리워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"업무와 개인 생활의 경계가 명확했던 여유로운 직장 문화가 그립고 아쉬워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"진로에 대한 무한한 가능성과 선택지가 있다고 믿었던 시절이 그리워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"용돈 관리만 하면 되었던 학생 시절의 경제적 단순함이 그립고 부러워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"부모님 덕분에 경제적 걱정 없이 공부에만 집중할 수 있었던 시절이 그리워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"작은 돈으로도 충분히 행복할 수 있었던 소박하고 순수한 소비 생활이 그리워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"첫 월급을 받았을 때의 뿌듯함과 경제적 독립에 대한 설렘이 그립고 소중해요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"물가가 지금보다 저렴해서 적은 돈으로도 여유로웠던 시절이 그립고 아쉬워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"투자나 재테크 걱정 없이 단순하게 저축만 했던 편안한 경제관이 그리워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"신용카드 없이도 현금으로 충분했던 간단한 소비 패턴이 그립고 좋았어요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"브랜드나 유행에 신경 쓰지 않고 필요한 것만 사던 실용적인 소비가 그리워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"경제적 여유가 있어서 가족이나 친구들에게 베풀 수 있었던 넉넉한 시절이 그리워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"미래에 대한 경제적 불안 없이 현재를 즐길 수 있었던 여유로운 마음이 그리워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"집값이 저렴해서 내 집 마련이 꿈이 아닌 현실이었던 시절이 그립고 부러워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"적금만으로도 목돈을 모을 수 있어서 투자 스트레스가 없었던 때가 그리워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"경제적 격차를 크게 느끼지 않고 친구들과 어울릴 수 있었던 시절이 그리워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"충동구매를 해도 큰 부담이 되지 않을 만큼 여유로웠던 경제 상황이 그립고 아쉬워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"노후 걱정 없이 현재를 마음껏 즐길 수 있었던 낙관적인 경제관이 그리워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"순수하고 호기심 가득했던 어린 시절의 마음과 세상을 보는 눈이 그리워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"상처받기 전의 순진하고 타인을 쉽게 믿었던 마음의 여유로움이 그립고 소중해요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"꿈과 이상으로 가득했던 젊은 시절의 열정과 에너지가 그립고 아쉬워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"복잡한 생각 없이 단순하게 행복할 수 있었던 마음의 평온함이 그리워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"실패를 두려워하지 않고 도전했던 용기와 자신감이 그립고 부러워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"감정을 솔직하게 표현할 수 있었던 자유롭고 진솔한 마음이 그리워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"미래에 대한 무한한 가능성을 믿었던 희망적이고 낙관적인 마음가짐이 그리워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"작은 것에도 크게 감동하고 기뻐했던 감수성이 풍부한 마음이 그립고 소중해요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"스트레스 없이 마음이 평안하고 여유로웠던 정신적 안정감이 그리워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"자기 자신을 사랑하고 받아들였던 건강한 자존감과 자신감이 그립고 아쉬워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"타인의 시선을 의식하지 않고 자유롭게 행동했던 순수한 마음이 그리워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"직감을 믿고 마음의 소리에 따라 결정했던 용기와 확신이 그립고 부러워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"매일을 새롭게 시작할 수 있다고 믿었던 긍정적이고 희망찬 마음이 그리워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"깊이 사색하고 성찰할 수 있는 여유와 집중력이 있었던 시절이 그리워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"감사한 마음으로 일상의 소소한 행복을 느꼈던 순수하고 맑은 마음이 그립고 소중해요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"어린 시절 부모님의 무조건적인 사랑과 보호를 받았던 안전감이 그립고 소중해요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"인간관계"
    }
  },
  {
    "content":"첫사랑과 함께했던 순수하고 떨렸던 감정들이 아련하고 그리워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"인간관계"
    }
  },
  {
    "content":"학창시절 매일 만나던 친구들과의 끈끈한 우정과 동지애가 그립고 아쉬워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"인간관계"
    }
  },
  {
    "content":"할머니, 할아버지와 함께 보냈던 따뜻하고 평화로운 시간들이 그리워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"인간관계"
    }
  },
  {
    "content":"연인과 함께 꿈꿨던 미래와 함께 만들어갔던 소중한 추억들이 아쉽고 그리워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"인간관계"
    }
  },
  {
    "content":"가족이 모두 함께 모여 밥을 먹고 이야기하던 화목한 시간이 그리워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"인간관계"
    }
  },
  {
    "content":"동네에서 자연스럽게 형성되었던 이웃들과의 인정 넘치는 관계가 그립고 아쉬워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"인간관계"
    }
  },
  {
    "content":"진솔하게 속마음을 나눌 수 있었던 깊은 우정과 신뢰 관계가 그리워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"인간관계"
    }
  },
  {
    "content":"무조건적으로 편을 들어주고 응원해주던 친구들의 우정이 소중하고 그리워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"인간관계"
    }
  },
  {
    "content":"연락하지 않아도 마음이 통했던 오랜 친구와의 편안한 관계가 그립고 아쉬워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"인간관계"
    }
  },
  {
    "content":"사소한 일상을 함께 나누며 서로를 돌봤던 가족들과의 유대감이 그리워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"인간관계"
    }
  },
  {
    "content":"갈등 없이 순수하게 즐거웠던 어린 시절 친구들과의 놀이 시간이 그리워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"인간관계"
    }
  },
  {
    "content":"서로의 꿈을 응원하고 격려해주던 동반자 같은 관계가 아쉽고 그리워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"인간관계"
    }
  },
  {
    "content":"멀리 떠난 친구들과 함께 만들었던 추억들이 지금은 소중한 보물 같아서 그리워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"인간관계"
    }
  },
  {
    "content":"세상 걱정 없이 웃고 떠들며 시간을 보냈던 순수한 관계들이 그립고 아쉬워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"인간관계"
    }
  },
  {
    "content":"어린 시절 생일이면 온 가족이 모여 축하해주던 특별하고 따뜻한 시간이 그리워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"졸업식에서 친구들과 함께 울고 웃으며 나눴던 진솔한 감정들이 아련하고 그리워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"첫 입학식의 설렘과 새로운 시작에 대한 기대감이 순수하고 그리워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"가족과 함께 보낸 명절의 따뜻함과 전통의 소중함을 느꼈던 시간이 그리워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"연인과 함께 맞이했던 기념일의 달콤함과 특별한 순간들이 아쉽고 그리워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"수능이나 입시 때의 긴장감과 열정, 그리고 동료애가 그립고 소중한 추억이에요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"결혼식 준비 과정에서 가족들과 함께 만들어갔던 행복한 기억들이 그리워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"첫 직장 입사식에서 느꼈던 사회인으로서의 자부심과 각오가 그립고 의미 있어요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"여행에서 만난 특별한 순간들과 그때의 자유로운 마음이 아쉽고 그리워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"가족의 회갑이나 칠순 같은 의미 있는 행사에서 느꼈던 감동이 그립고 소중해요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"친구의 결혼식에서 함께 기뻐하고 축복했던 순수한 마음이 그리워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"새해 첫날의 희망찬 마음과 새로운 계획에 대한 설렘이 그립고 아쉬워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"크리스마스나 연말 모임에서 느꼈던 따뜻한 연대감과 사랑이 그리워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"중요한 시험에 합격했을 때의 기쁨과 성취감, 그리고 축하받던 순간이 그리워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"어린 시절 여름휴가나 겨울방학의 자유로움과 무한한 가능성이 그립고 소중해요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"처음 창작을 시작했을 때의 순수한 열정과 무한한 가능성에 대한 믿음이 그리워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"실력에 대한 부담 없이 자유롭게 표현했던 창작 초기의 즐거움이 그립고 소중해요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"멘토나 스승과 함께 배우고 성장했던 따뜻한 사제관계가 그립고 아쉬워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"작은 발전에도 크게 기뻐하고 성취감을 느꼈던 순수한 마음이 그리워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"경쟁이나 평가 없이 오로지 즐거움으로 창작했던 시절이 그립고 부러워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"새로운 기법이나 스타일을 배우는 것이 신나고 기대되던 호기심 가득한 시절이 그리워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"창작 동료들과 함께 고민하고 격려하며 성장했던 동반자적 관계가 그립고 소중해요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"실패를 두려워하지 않고 과감하게 실험했던 도전 정신이 그립고 아쉬워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"영감이 넘쳐나서 아이디어가 끊임없이 떠올랐던 창의적인 시절이 그리워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"순수하게 예술 자체를 사랑했던 마음과 창작에 대한 열정이 그립고 소중해요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"시간 가는 줄 모르고 몰입했던 창작의 즐거움과 몰입감이 그리워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"다른 사람의 시선을 의식하지 않고 자유롭게 표현했던 용기가 그립고 부러워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"작품을 완성했을 때의 순수한 기쁨과 성취감이 그립고 아쉬워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"배우고 성장하는 과정 자체가 즐거웠던 학습에 대한 열정이 그리워요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"꿈과 목표가 명확했고 그것을 향해 나아가는 확신이 있었던 시절이 그립고 소중해요.",
    "metadata":{
      "emotion":"그리움과 아쉬움",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"새로운 취미를 시작하고 싶은 강한 욕구가 생겨서 여러 활동을 알아보고 있어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"더 건강한 생활을 하고 싶다는 동기로 매일 운동 계획을 세우고 실천하려고 해요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"주말마다 새로운 카페나 맛집을 찾아다니고 싶은 탐험 욕구가 강해져요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"집을 더 아늑하고 예쁘게 꾸미고 싶어서 인테리어에 대한 욕심이 생겼어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"요리 실력을 늘리고 싶은 마음에 새로운 레시피에 도전하고 싶어져요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"반려동물과 더 많은 시간을 보내고 싶어서 여행 계획을 세우고 있어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"독서량을 늘리고 싶은 욕구로 매일 조금씩이라도 책을 읽으려고 노력해요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"정원 가꾸기에 도전해서 직접 기른 채소를 먹어보고 싶다는 욕구가 생겼어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"새로운 언어를 배워서 다른 나라 사람들과 소통하고 싶은 동기가 강해요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"여행을 통해 다양한 문화를 경험하고 견문을 넓히고 싶은 욕구가 커져요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"미니멀 라이프를 실천해서 더 단순하고 의미 있는 삶을 살고 싶어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"사진 촬영 기술을 배워서 일상의 아름다운 순간들을 기록하고 싶어져요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"새로운 동네로 이사가서 다른 환경에서 생활해보고 싶은 욕구가 있어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"자연과 더 가까이에서 생활하고 싶어서 캠핑이나 등산을 시작하려고 해요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"손으로 무언가를 만드는 활동을 통해 성취감을 느끼고 싶은 욕구가 생겼어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"건강한 몸을 만들고 싶은 강한 동기로 규칙적인 운동을 시작했어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"체중 감량에 성공해서 더 자신감 있는 모습이 되고 싶은 욕구가 커요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"금연이나 금주에 성공해서 더 건강한 생활을 하고 싶은 동기가 강해져요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"스트레스 관리법을 배워서 정신적으로 더 안정되고 싶어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"올바른 식습관을 만들어서 몸의 컨디션을 개선하고 싶은 욕구가 있어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"요가나 명상을 통해 몸과 마음의 균형을 찾고 싶어져요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"정기 건강검진을 받아서 질병을 예방하고 싶은 동기가 생겼어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"마라톤 완주나 운동 목표를 달성해서 성취감을 느끼고 싶어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"수면의 질을 높여서 더 활기찬 하루하루를 보내고 싶은 욕구가 강해요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"가족의 건강을 지키고 싶어서 건강한 생활 습관을 함께 만들려고 해요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"면역력을 키워서 질병에 강한 몸을 만들고 싶은 동기가 있어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"노화를 늦추고 싶어서 안티에이징에 관심을 갖고 실천하려고 해요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"재활 치료를 통해 기능을 회복하고 싶은 강한 의지가 생겼어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"건강한 노년을 준비하고 싶어서 지금부터 관리를 시작하려고 해요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"가족력이 있는 질병을 예방하고 싶어서 생활 습관을 개선하고 있어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"새로운 디지털 기술을 배워서 시대에 뒤떨어지지 않고 싶은 동기가 강해요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"온라인에서 영향력 있는 콘텐츠를 만들어서 많은 사람들과 소통하고 싶어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"디지털 마케팅을 배워서 온라인 사업을 시작하고 싶은 욕구가 커져요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"SNS를 통해 개인 브랜딩을 하고 싶어서 콘텐츠 제작에 도전하고 있어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"온라인 강의를 통해 새로운 지식과 기술을 습득하고 싶은 동기가 있어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"유튜브나 블로그를 통해 나만의 채널을 성공시키고 싶은 욕구가 강해져요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"디지털 아트나 디자인을 배워서 창작 활동을 하고 싶어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"온라인 커뮤니티에서 리더 역할을 하고 싶은 욕구가 생겼어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"프로그래밍을 배워서 나만의 앱이나 웹사이트를 만들고 싶어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"온라인 쇼핑몰을 운영해서 성공적인 이커머스 사업을 하고 싶어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"가상현실이나 메타버스 같은 신기술을 체험하고 활용하고 싶어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"온라인에서 교육 콘텐츠를 제작해서 지식을 나누고 싶은 욕구가 있어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"디지털 노마드가 되어서 자유로운 삶을 살고 싶은 동기가 강해져요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"인공지능이나 빅데이터 같은 최신 기술을 활용하고 싶어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"온라인 게임에서 프로급 실력을 갖추고 싶은 욕구가 커지고 있어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"새로운 분야에 도전해서 전문성을 키우고 싶은 강한 동기가 생겨났어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"승진하고 싶은 욕구로 업무 능력 향상을 위해 더 열심히 노력하고 있어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"창업에 대한 꿈이 커져서 사업 아이템을 찾고 공부하고 싶어져요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"해외에서 일하고 싶은 욕구로 영어 실력 향상에 더 집중하려고 해요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"새로운 기술을 습득해서 업무 효율성을 높이고 싶은 동기가 강해요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"대학원에 진학해서 더 깊이 있는 학문을 탐구하고 싶은 욕구가 있어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"리더십을 발휘할 수 있는 역할을 맡아서 팀을 이끌어보고 싶어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"자격증을 취득해서 전문성을 인정받고 싶은 동기로 공부에 매진하고 있어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"다른 업계로 이직해서 새로운 경험을 쌓고 싶은 욕구가 커져요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"연구나 개발 분야에서 혁신적인 성과를 내고 싶은 야심이 생겼어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"멘토링을 통해 후배들에게 도움을 주고 싶은 욕구가 강해져요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"국제적인 프로젝트에 참여해서 글로벌 경험을 쌓고 싶어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"업무와 삶의 균형을 더 잘 맞추고 싶어서 시간 관리법을 배우고 있어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"프리랜서로 독립해서 자유로운 업무 환경을 만들고 싶은 욕구가 있어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"사회에 기여할 수 있는 의미 있는 일을 하고 싶다는 동기가 강해져요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"경제적 자유를 얻고 싶은 강한 동기로 투자 공부를 시작했어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"내 집 마련의 꿈을 이루고 싶어서 저축과 재테크에 집중하고 있어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"부업을 통해 추가 수입을 만들고 싶은 욕구로 여러 방법을 알아보고 있어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"가족에게 더 좋은 환경을 제공하고 싶어서 수입 증대를 위해 노력해요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"여행 자금을 모아서 꿈꿔왔던 해외여행을 가고 싶은 동기가 강해져요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"자녀 교육비를 준비하고 싶어서 장기적인 재정 계획을 세우고 있어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"노후 준비를 제대로 하고 싶은 욕구로 연금과 보험을 알아보고 있어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"빚을 모두 갚고 부채 없는 생활을 하고 싶다는 강한 동기가 생겼어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"창업 자금을 모아서 자신의 사업을 시작하고 싶은 욕구가 커져요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"가족이나 친구들에게 베풀 수 있을 만큼 여유로워지고 싶어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"명품이나 고급 제품을 구매할 수 있는 경제력을 갖고 싶은 욕구가 있어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"투자를 통해 자산을 늘려서 경제적 안정을 얻고 싶은 동기가 강해요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"합리적인 소비 습관을 만들어서 가계를 더 효율적으로 관리하고 싶어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"부모님께 효도하고 싶어서 경제적 능력을 키우려고 노력하고 있어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"사회적 기부나 나눔을 할 수 있을 만큼 성공하고 싶은 욕구가 있어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"자기 계발을 통해 더 나은 사람이 되고 싶은 강한 동기가 생겼어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"마음의 평화를 찾고 싶어서 명상이나 영성 수련에 관심이 커져요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"감정 조절 능력을 키워서 더 성숙한 인간이 되고 싶은 욕구가 있어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"자신감을 회복하고 싶어서 심리 상담이나 치료를 받아보려고 해요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"인생의 목적과 의미를 찾고 싶어서 철학이나 종교에 관심을 갖고 있어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"과거의 상처를 치유하고 싶어서 용서와 화해의 마음을 기르려고 해요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"창의성을 개발하고 싶어서 예술 활동이나 상상력 훈련을 하고 있어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"스트레스 관리 능력을 키워서 마음의 안정을 유지하고 싶어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"감사하는 마음을 기르고 싶어서 일상의 소소한 행복을 찾으려고 노력해요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"자아 정체성을 확립하고 싶어서 진정한 나 자신을 탐구하고 있어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"긍정적인 사고방식을 기르고 싶어서 부정적인 생각을 바꾸려고 해요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"리더십과 카리스마를 기르고 싶어서 인격 수양에 힘쓰고 있어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"집중력과 몰입력을 높이고 싶어서 미니멀라이프를 실천하려고 해요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"직감과 내적 지혜를 기르고 싶어서 내면의 목소리에 귀 기울이고 있어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"자기 사랑과 자존감을 높이고 싶어서 스스로를 돌보는 법을 배우고 있어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"새로운 사람들과 만나서 인맥을 넓히고 싶은 욕구로 모임에 적극 참여하고 있어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"인간관계"
    }
  },
  {
    "content":"가족과의 관계를 더 돈독하게 만들고 싶어서 함께 보내는 시간을 늘리려고 해요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"인간관계"
    }
  },
  {
    "content":"진정한 친구를 사귀고 싶은 마음에 진솔한 대화를 나눌 수 있는 사람을 찾고 있어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"인간관계"
    }
  },
  {
    "content":"연인을 만나서 사랑을 경험하고 싶다는 욕구로 새로운 만남에 열려있어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"인간관계"
    }
  },
  {
    "content":"의미 있는 멘토를 찾아서 인생 조언을 받고 싶은 동기가 강해져요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"인간관계"
    }
  },
  {
    "content":"다른 사람들에게 도움이 되고 싶어서 봉사 활동에 참여하려고 해요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"인간관계"
    }
  },
  {
    "content":"갈등 관계를 회복하고 싶어서 먼저 화해의 손길을 내밀고 싶어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"인간관계"
    }
  },
  {
    "content":"소통 능력을 키워서 더 깊이 있는 관계를 만들고 싶은 욕구가 있어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"인간관계"
    }
  },
  {
    "content":"결혼해서 안정적인 가정을 꾸리고 싶다는 강한 동기가 생겼어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"인간관계"
    }
  },
  {
    "content":"동료들과 더 좋은 팀워크를 만들어서 함께 성장하고 싶어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"인간관계"
    }
  },
  {
    "content":"이웃들과 친해져서 따뜻한 지역 공동체를 만들고 싶은 욕구가 있어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"인간관계"
    }
  },
  {
    "content":"SNS를 통해 더 많은 사람들과 소통하고 네트워킹하고 싶어져요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"인간관계"
    }
  },
  {
    "content":"갈등 해결 능력을 키워서 중재자 역할을 하고 싶은 동기가 생겼어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"인간관계"
    }
  },
  {
    "content":"다양한 연령대의 사람들과 교류해서 세대 간 이해를 높이고 싶어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"인간관계"
    }
  },
  {
    "content":"국제적인 친구들을 사귀어서 다문화적 관계를 경험하고 싶은 욕구가 있어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"인간관계"
    }
  },
  {
    "content":"완벽한 결혼식을 올리고 싶은 욕구로 세심하게 준비하고 계획하고 있어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"중요한 시험에 합격해서 인생의 전환점을 만들고 싶은 강한 동기가 있어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"의미 있는 생일 파티를 열어서 소중한 사람들과 추억을 만들고 싶어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"졸업 후 꿈의 직장에 입사하고 싶어서 취업 준비에 모든 것을 쏟고 있어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"가족의 특별한 기념일을 성대하게 축하해주고 싶은 마음이 커요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"이사해서 새로운 환경에서 새로운 시작을 하고 싶은 욕구가 강해져요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"여행에서 평생 잊지 못할 특별한 경험을 만들고 싶어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"중요한 발표나 공연에서 성공적인 결과를 내고 싶은 동기가 강해요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"새해에는 작년보다 더 발전된 모습이 되고 싶다는 다짐이 강해져요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"승진이나 승격의 기회를 잡아서 커리어 발전을 이루고 싶어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"첫 아이 출산을 앞두고 좋은 부모가 되고 싶은 욕구가 간절해요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"은퇴 후에도 의미 있는 활동을 하고 싶어서 미리 계획을 세우고 있어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"중요한 계약이나 거래에서 성공해서 사업을 발전시키고 싶어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"가족의 건강 회복을 위해 최선을 다하고 싶은 간절한 마음이 있어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"새로운 도전을 통해 자신의 한계를 뛰어넘고 싶은 동기가 강해져요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"예술 작품을 완성해서 사람들에게 감동을 주고 싶은 강한 욕구가 있어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"새로운 창작 기법을 배워서 표현의 폭을 넓히고 싶은 동기가 커져요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"작가나 예술가로서 인정받고 싶어서 꾸준히 작품 활동을 하고 있어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"창작을 통해 사회적 메시지를 전달하고 싶은 욕구가 강해져요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"나만의 독창적인 스타일을 개발하고 싶어서 다양한 시도를 하고 있어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"창작 동료들과 함께 성장하고 싶어서 스터디나 모임에 참여하고 있어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"대중들에게 사랑받는 작품을 만들고 싶은 꿈과 욕구가 강해요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"창작 실력을 늘리고 싶어서 전문 교육을 받거나 워크숍에 참여하려고 해요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"전시회나 공연을 통해 작품을 발표하고 싶은 동기가 생겼어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"창작을 통해 개인적 치유와 성장을 경험하고 싶은 욕구가 있어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"멘토를 찾아서 창작 여정에서 조언과 지도를 받고 싶어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"창작으로 생계를 유지할 수 있는 전문가가 되고 싶은 꿈이 있어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"다양한 장르와 매체에 도전해서 창작 영역을 확장하고 싶어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"창작을 통해 문화 발전에 기여하고 싶은 사명감이 생겼어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"후배들에게 창작의 즐거움을 전해주고 싶어서 교육 활동을 하고 싶어요.",
    "metadata":{
      "emotion":"동기와 욕구",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"동네 카페에서 단골이 되면서 사장님과 친해진 것이 일상에 따뜻함을 더해줘요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"취미 모임에서 비슷한 관심사를 가진 사람들과 만나면서 소속감을 느끼고 있어요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"이웃들과 인사를 나누며 지내니까 우리 동네가 더 정겹고 안전하게 느껴져요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"친구들과 함께 요리하고 나누어 먹는 시간이 혼자일 때보다 훨씬 즐거워요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"운동 친구들과 함께 운동하니까 동기부여도 되고 재미도 배가 되는 것 같아요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"가족과 함께 보내는 저녁 시간이 하루의 피로를 잊게 해주는 소중한 시간이에요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"동호회 활동을 통해 나이대가 다른 사람들과 어울리면서 시야가 넓어졌어요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"반려동물을 기르면서 동물병원이나 애견카페에서 새로운 인연들을 만나고 있어요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"주말마다 가족들과 함께하는 나들이가 서로를 더 잘 이해하게 해주는 시간이에요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"독서 모임에서 책에 대해 토론하면서 다른 사람들의 생각을 듣는 재미가 쏠쏠해요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"동네 축제나 행사에 참여하면서 지역 주민들과의 유대감이 깊어지고 있어요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"친구와 함께 새로운 취미를 시작하니까 혼자였다면 포기했을 일도 계속하게 돼요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"가족들과 함께 여행을 다니면서 평소에 나누지 못했던 깊은 대화를 나누게 돼요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"산책 중에 만나는 동네 어르신들과 대화를 나누는 것이 마음을 따뜻하게 해줘요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"온 가족이 함께 TV를 보며 웃고 떠드는 시간이 가장 행복하고 평화로운 순간이에요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"가족이 아플 때 함께 병원에 가서 곁에 있어주는 것만으로도 위로가 되는 것 같아요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"운동 친구들과 함께 건강 관리를 하니까 혼자일 때보다 지속력이 생겨요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"의료진과의 신뢰 관계가 형성되면 치료 과정이 더 편안하고 효과적인 것 같아요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"같은 질병을 앓는 환우들과 만나서 경험을 나누니까 혼자가 아니라는 위로를 받아요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"가족들이 내 건강을 걱정해주고 돌봐주는 마음이 치료에 큰 힘이 되어주고 있어요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"건강 검진을 함께 받은 친구와 결과를 공유하며 서로 격려하고 있어요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"재활 치료 과정에서 치료사와의 좋은 관계가 회복 의지를 북돋아주고 있어요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"다이어트를 함께 하는 친구가 있어서 서로 동기부여가 되고 포기하지 않게 돼요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"정신적으로 힘들 때 주변 사람들의 따뜻한 관심과 격려가 큰 위로가 되어줘요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"건강한 식단을 가족들과 함께 실천하니까 서로에게 좋은 영향을 주고받고 있어요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"병원에서 만난 의료진의 친절하고 세심한 배려가 치료에 대한 신뢰를 높여줘요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"건강 관련 모임에서 만난 사람들과 정보를 공유하며 도움을 주고받고 있어요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"가족의 건강 회복을 위해 모두가 함께 노력하는 과정에서 유대감이 더욱 깊어져요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"요가나 명상 수업에서 만난 사람들과 마음의 평화를 함께 찾아가는 기분이에요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"건강을 위한 취미 활동을 통해 새로운 사람들과 만나면서 삶의 활력을 얻고 있어요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"SNS를 통해 오랫동안 연락하지 못했던 친구들과 다시 연결되는 반가움이 특별해요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"온라인 커뮤니티에서 같은 관심사를 가진 사람들과 소통하며 소속감을 느끼고 있어요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"가족들과 단체 채팅방에서 일상을 공유하며 거리가 떨어져 있어도 가까움을 느껴요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"온라인 게임에서 만난 팀원들과 협력하며 가상 공간에서의 우정을 쌓아가고 있어요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"화상통화로 멀리 있는 가족과 얼굴을 보며 대화할 수 있어서 거리감이 줄어들어요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"온라인 스터디 그룹에서 서로 격려하고 정보를 공유하며 함께 성장하고 있어요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"블로그나 유튜브를 통해 구독자들과 소통하면서 새로운 형태의 관계를 경험해요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"온라인 쇼핑 후기나 추천을 통해 다른 사람들과 정보를 나누는 재미가 쏠쏠해요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"디지털 기기 사용법을 가족들에게 알려주면서 세대 간 소통의 다리 역할을 하고 있어요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"온라인 모임이나 웨비나에 참여하면서 지역의 제약 없이 다양한 사람들과 만나고 있어요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"SNS에서 받는 댓글이나 반응이 일상에 작은 기쁨과 연결감을 주고 있어요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"온라인 펀딩이나 기부를 통해 좋은 목적에 함께 동참하는 연대감을 느껴요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"디지털 플랫폼을 통해 창작물을 공유하고 피드백을 받으면서 창작 동기를 얻고 있어요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"온라인 교육 플랫폼에서 강사와 수강생들과의 상호작용이 학습 효과를 높여줘요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"가상현실이나 메타버스에서 새로운 형태의 사회적 경험을 하는 것이 신선하고 흥미로워요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"동료들과의 협업이 잘 이루어질 때 혼자서는 불가능했을 성과를 만들어내는 기쁨이 있어요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"상사로부터 인정받고 격려받을 때 더 열심히 일하고 싶은 동기가 생겨나요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"신입사원을 멘토링하면서 가르치는 즐거움과 보람을 느끼고 있어요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"팀 프로젝트에서 각자의 강점을 살려 협력할 때 시너지 효과를 실감해요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"학습 스터디 그룹에서 서로 질문하고 설명하면서 이해도가 훨씬 높아져요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"직장 동료들과 퇴근 후 식사하며 나누는 대화가 업무 스트레스를 해소해줘요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"다른 부서 사람들과 협업하면서 회사 전체에 대한 이해의 폭이 넓어졌어요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"외부 교육에서 만난 다른 회사 사람들과 네트워킹하는 것이 시야를 넓혀줘요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"동기들과 함께 성장해나가는 과정에서 건전한 경쟁 의식과 동지애를 느껴요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"상급자의 조언과 피드백을 받을 때 혼자서는 발견하지 못한 개선점을 알게 돼요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"후배들과 함께 일하면서 그들의 신선한 아이디어에서 영감을 받고 있어요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"온라인 강의에서 다른 수강생들과 토론하면서 다양한 관점을 접하게 돼요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"업무 관련 컨퍼런스에서 전문가들과 대화하며 새로운 인사이트를 얻어요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"팀 빌딩 활동을 통해 동료들과 더 가까워지고 업무 협력도 원활해졌어요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"멘토로부터 받는 조언이 커리어 방향을 정하는 데 큰 도움이 되고 있어요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"가족을 위해 경제적 책임을 다할 때 가장의 역할에 대한 보람과 자부심을 느껴요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"친구들과 함께 공동구매를 하면서 경제적 절약과 함께 유대감도 쌓고 있어요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"투자 모임에서 다른 사람들과 정보를 공유하며 함께 성장하는 재미가 있어요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"가족의 경제적 어려움을 함께 극복해나가면서 서로에 대한 신뢰가 깊어져요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"동료들과 합리적인 소비 팁을 나누면서 서로에게 도움이 되는 관계를 만들어가고 있어요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"부모님께 용돈을 드릴 수 있게 되면서 효도하는 기쁨과 성장한 느낌이 들어요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"친구들과 여행 경비를 함께 모으고 계획하는 과정에서 협력하는 즐거움을 느껴요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"경제적으로 어려운 친구를 도와줄 수 있어서 우정의 진정한 가치를 실감해요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"가족들과 가계 운영에 대해 함께 논의하면서 책임감과 소속감을 느끼고 있어요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"동네 상권을 이용하면서 지역 경제에 기여한다는 뿌듯함과 공동체 의식을 느껴요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"재테크 스터디에서 만난 사람들과 경제적 목표를 공유하며 동기부여를 받고 있어요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"가족의 꿈을 위해 함께 저축하는 과정에서 공동의 목표 달성에 대한 설렘이 있어요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"경제적 성공을 가족이나 친구들과 나누면서 혼자만의 기쁨보다 더 큰 만족감을 느껴요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"어려운 이웃을 도울 수 있는 경제적 여유가 생겼을 때 사회 구성원으로서의 보람을 느껴요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"금융 상품에 대해 지인들과 정보를 교환하면서 현명한 선택을 할 수 있게 돼요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"깊은 우정을 통해 진정한 나 자신을 받아들이고 사랑하는 법을 배우고 있어요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"가족과의 관계에서 무조건적인 사랑의 의미를 깨닫고 내면의 안정감을 찾아요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"연인과의 관계를 통해 상대방을 이해하고 배려하는 마음이 성장하고 있어요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"친구들과의 진솔한 대화를 통해 내 감정을 표현하고 정리하는 능력이 늘고 있어요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"다른 사람들과의 갈등을 해결하면서 인내심과 포용력이 커지는 것을 느껴요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"타인을 도우면서 느끼는 보람이 내 존재의 의미와 가치를 깨닫게 해줘요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"사회적 관계에서의 실수를 통해 겸손함과 성찰의 중요성을 배우고 있어요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"다양한 사람들과의 만남을 통해 편견을 버리고 열린 마음을 기르게 됐어요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"공동체 활동에 참여하면서 개인을 넘어선 더 큰 목적에 대한 의식이 생겼어요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"인간관계에서 받은 상처를 치유하면서 용서와 화해의 힘을 체험하고 있어요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"타인의 감정에 공감하는 능력이 늘면서 더 따뜻한 사람이 되어가는 것 같아요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"사회적 책임감을 느끼면서 개인의 성장이 공동체에 미치는 영향을 생각하게 됐어요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"다른 문화권 사람들과의 교류를 통해 다양성을 수용하는 마음이 넓어졌어요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"세대 간 소통을 통해 지혜와 경험의 소중함을 깨닫고 겸허한 마음을 갖게 됐어요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"인간관계의 깊이를 통해 진정한 행복은 혼자가 아닌 함께할 때 온다는 것을 느껴요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"오랜 친구와 만나서 변함없는 우정을 확인할 때 인생에서 가장 소중한 것을 느껴요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"인간관계"
    }
  },
  {
    "content":"새로운 사람과 깊은 대화를 나누면서 서로를 이해해가는 과정이 설레고 의미 있어요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"인간관계"
    }
  },
  {
    "content":"가족들과 갈등을 해결하고 화해했을 때 관계가 더 단단해지는 것을 경험해요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"인간관계"
    }
  },
  {
    "content":"연인과 함께 보내는 시간이 세상에서 가장 편안하고 행복한 순간이에요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"인간관계"
    }
  },
  {
    "content":"친구가 어려울 때 도움을 줄 수 있어서 우정의 진정한 의미를 느끼고 있어요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"인간관계"
    }
  },
  {
    "content":"부모님과 성인이 되어서 나누는 대화가 예전과 달리 동등한 관계로 발전한 것 같아요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"인간관계"
    }
  },
  {
    "content":"새로운 환경에서 만난 사람들과 친해지면서 인간관계의 소중함을 다시 깨달아요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"인간관계"
    }
  },
  {
    "content":"연인과의 관계에서 서로를 있는 그대로 받아들일 때 진정한 사랑을 느껴요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"인간관계"
    }
  },
  {
    "content":"친구들과 함께 어려운 시기를 극복하면서 우정이 더욱 깊어지는 것을 경험해요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"인간관계"
    }
  },
  {
    "content":"가족 모임에서 여러 세대가 함께 어울리며 느끼는 유대감이 특별하고 따뜻해요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"인간관계"
    }
  },
  {
    "content":"갈등이 있던 사람과 진솔한 대화를 통해 오해를 풀었을 때 관계 회복의 기쁨을 느껴요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"인간관계"
    }
  },
  {
    "content":"연인과 함께 미래를 계획하면서 공동의 꿈을 꾸는 설렘과 안정감을 느껴요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"인간관계"
    }
  },
  {
    "content":"친구의 성공을 진심으로 축하하면서 질투 없는 순수한 우정의 아름다움을 느껴요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"인간관계"
    }
  },
  {
    "content":"가족의 무조건적인 사랑과 지지를 받을 때 세상에서 가장 든든한 버팀목을 느껴요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"인간관계"
    }
  },
  {
    "content":"새로운 사람들과 만나면서 내 자신도 새로운 면을 발견하게 되는 신선함이 있어요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"인간관계"
    }
  },
  {
    "content":"결혼식을 준비하면서 가족과 친구들의 축복과 도움을 받는 것이 감동적이고 고마워요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"생일에 소중한 사람들이 축하해주는 것만으로도 하루가 특별하고 의미 있게 느껴져요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"졸업식에서 가족들이 자랑스러워하는 모습을 보니 그동안의 노력이 보상받는 기분이에요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"승진 소식을 들었을 때 동료들이 진심으로 축하해주어서 성취의 기쁨이 배가 돼요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"가족의 중요한 기념일을 함께 축하하면서 유대감과 전통의 소중함을 느껴요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"친구의 결혼식에 참석해서 인생의 중요한 순간을 함께 나누는 특별함을 느껴요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"명절에 온 가족이 모여서 보내는 시간이 그 어떤 선물보다 소중하고 값져요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"새해를 사랑하는 사람들과 함께 맞이하면서 희망찬 시작에 대한 설렘을 공유해요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"입학식이나 입사식에서 가족의 응원을 받으며 새로운 출발에 대한 용기를 얻어요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"친구들과 함께 특별한 이벤트를 기획하고 실행하는 과정에서 협력의 즐거움을 느껴요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"어려운 시험을 통과했을 때 가족과 친구들이 더 기뻐해주어서 성취감이 더욱 커져요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"이사를 하면서 새로운 이웃들을 만나고 지역 사회에 적응해가는 과정이 흥미로워요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"가족의 회갑이나 고희 같은 의미 있는 행사를 준비하면서 효도의 기쁨을 느껴요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"여행에서 현지 사람들과 만나서 나누는 소통이 여행을 더욱 풍성하게 만들어줘요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"중요한 발표나 공연에서 가족과 친구들의 응원이 긴장을 이기고 최선을 다하게 해줘요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"창작 동료들과 함께 작업하면서 혼자서는 불가능했을 아이디어와 영감을 얻고 있어요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"멘토의 조언과 격려를 받으면서 창작 여정에서 방향을 잃지 않고 나아갈 수 있어요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"작품에 대한 다른 사람들의 피드백이 성장의 원동력이 되고 새로운 관점을 제공해줘요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"창작 모임에서 만난 사람들과 서로의 작품을 공유하며 동기부여를 받고 있어요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"선배 창작자들의 경험담을 들으면서 어려움을 극복할 용기와 지혜를 얻어요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"후배들에게 창작 기법을 가르치면서 나 자신도 기초를 다시 돌아보는 계기가 돼요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"전시회나 공연에서 관객들과 소통하면서 창작의 진정한 의미를 깨닫게 돼요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"창작 과정에서 겪는 어려움을 동료들과 나누면서 혼자가 아니라는 위로를 받아요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"다른 분야 창작자들과의 교류를 통해 창작의 영역을 확장하는 영감을 얻고 있어요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"창작 워크숍에서 다양한 사람들과 함께 작업하면서 협업의 즐거움을 경험해요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"비평가나 전문가들의 조언을 통해 작품의 완성도를 높이는 방법을 배우고 있어요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"창작을 통해 사회적 메시지를 전달하고 사람들과 소통하는 보람을 느껴요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"온라인을 통해 전 세계 창작자들과 교류하면서 글로벌한 시각을 갖게 됐어요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"창작 스터디 그룹에서 함께 성장해나가는 동반자적 관계가 가장 소중한 자산이에요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"내 작품이 다른 사람들에게 영감을 주고 영향을 미칠 때 창작자로서의 사명감을 느껴요.",
    "metadata":{
      "emotion":"사회적 관계 감정",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"주말 오후 햇살이 들어오는 창가에서 책을 읽으니 마음이 평온하고 여유로워요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"바쁜 일상에서 벗어나 온천에서 보내는 시간이 몸과 마음을 완전히 이완시켜줘요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"요즘 특별히 하고 싶은 일이 없어서 집에서 아무것도 안 하고 멍하니 있는 시간이 많아져요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"반복되는 일상에 지쳐서 새로운 자극이나 변화 없이 그냥 흘러가는 대로 살고 있어요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"정원에서 꽃을 가꾸며 보내는 조용한 시간이 스트레스를 모두 날려 보내 줘요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"취미 활동에 대한 열정이 식어서 예전만큼 재미를 느끼지 못하고 있어요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"커피 한 잔과 함께 창밖을 바라보는 여유로운 아침이 하루를 평화롭게 시작하게 해줘요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"매일 똑같은 루틴에 매몰되어서 삶이 지루하고 활력이 없는 것 같아요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"자연 속에서 산책하며 새소리를 듣는 것만으로도 마음의 평정을 찾을 수 있어요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"예전에 즐겨하던 활동들이 이제는 귀찮고 의욕이 생기지 않아서 미루고만 있어요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"따뜻한 욕조에 몸을 담그고 있으니 모든 피로와 긴장이 풀리는 기분이에요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"일상에서 특별함을 찾지 못해서 매일이 무색무미하게 지나가는 것 같아요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"좋아하는 음악을 들으며 소파에 누워있는 시간이 가장 편안하고 자유로워요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"집안일조차 귀찮아서 미루게 되고 정리되지 않은 공간에서 답답함을 느껴요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"명상이나 요가를 통해 내면의 고요함과 안정감을 찾아가는 시간이 소중해요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"마사지나 스파에서 받는 치료가 몸의 긴장을 완전히 풀어주고 힐링이 돼요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"건강 관리에 대한 의욕이 떨어져서 운동이나 식단 관리를 소홀히 하고 있어요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"따뜻한 찜질방에서 보내는 시간이 몸의 피로와 스트레스를 모두 날려 보내줘요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"만성적인 피로감으로 인해 활동량이 줄어들고 집에서만 쉬려고 해요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"요가나 태극권 같은 부드러운 운동이 몸과 마음의 균형을 찾아주는 것 같아요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"건강에 대한 관심이 예전만큼 없어져서 정기 검진도 미루고 있어요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"자연 속에서 삼림욕을 하며 깊게 숨쉬는 시간이 폐와 마음을 정화시켜줘요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"몸의 컨디션이 좋지 않아서 평소보다 활동적이지 못하고 쉬는 시간이 많아졌어요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"명상이나 호흡법을 통해 마음의 안정을 찾고 스트레스를 해소하고 있어요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"건강한 생활습관을 유지할 동기가 부족해서 기존 루틴이 흐트러지고 있어요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"온천이나 족욕을 통해 혈액순환이 개선되고 몸 전체가 이완되는 느낌을 받아요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"체력 저하로 인해 예전만큼 활발한 활동을 하기 어려워서 소극적이 됐어요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"아로마테라피나 음악 치료를 통해 정신적 안정과 평화로움을 찾고 있어요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"수면 패턴이 불규칙해져서 낮에 피로감을 느끼고 의욕이 떨어져요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"자연 치유나 대체 의학에 관심을 갖고 몸의 자연스러운 회복력을 믿고 있어요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"스마트폰을 멀리 두고 디지털 디톡스 시간을 가지니 마음이 한결 평온해져요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"온라인 활동에 대한 관심이 줄어들어서 SNS 업데이트도 자주 하지 않게 됐어요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"인터넷 서핑을 하며 아무 목적 없이 시간을 보내는 것이 때로는 휴식이 돼요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"디지털 기기 사용을 줄이고 아날로그적인 활동에서 진정한 여유를 찾고 있어요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"온라인 게임이나 엔터테인먼트 콘텐츠 시청으로 현실에서 벗어나는 시간을 가져요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"새로운 앱이나 기술에 대한 호기심이 예전만큼 크지 않아서 기존 것만 사용해요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"온라인 명상 앱이나 수면 유도 앱을 통해 마음의 안정을 찾고 있어요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"디지털 콘텐츠 소비량이 줄어들어서 수동적으로 정보를 받아들이는 시간이 많아졌어요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"자연 소리나 백색 소음 앱을 들으며 집중력을 높이고 마음을 진정시켜요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"온라인에서의 사회적 활동에 참여하는 빈도가 현저히 줄어들었어요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"유튜브나 넷플릭스를 보며 아무 생각 없이 시간을 보내는 것이 휴식이 돼요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"디지털 기술 발전을 따라가려는 의욕이 떨어져서 필수적인 것만 사용하고 있어요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"온라인 쇼핑을 하며 창 여러 개를 열어놓고 구경만 하는 시간이 스트레스 해소가 돼요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"인터넷에서 새로운 정보를 찾거나 학습할 동기가 부족해서 소극적이 됐어요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"디지털 미니멀리즘을 실천하며 꼭 필요한 앱과 서비스만 사용하고 있어요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"프로젝트가 마무리된 후 잠시 여유를 갖고 휴식하는 시간이 재충전에 도움이 돼요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"업무에 대한 열정이 식어서 매일 출근하는 것조차 의미를 찾지 못하겠어요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"점심시간에 사무실 옥상에서 바람을 쌀며 보내는 시간이 오후 업무 활력을 줘요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"승진에서 누락된 후 업무에 대한 동기가 떨어져서 최소한의 일만 하고 있어요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"연수 프로그램에서 동료들과 여유롭게 대화하며 보내는 시간이 스트레스 해소에 좋아요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"새로운 도전이나 성장 기회가 없어서 현재 위치에서 정체되어 있는 기분이에요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"퇴근 후 집에 와서 업무 생각을 완전히 내려놓고 쉴 수 있는 시간이 행복해요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"학습에 대한 의욕이 떨어져서 새로운 지식을 익히려는 노력을 기울이지 않고 있어요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"바쁜 업무 중간에 잠깐 차 한잔 마시며 창밖을 바라보는 것만으로도 마음이 진정돼요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"업무 루틴이 너무 익숙해져서 자동으로 처리하다 보니 성취감이나 만족감이 없어요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"워케이션이나 원격근무로 환경을 바꿔서 일하니 마음이 편안하고 집중도 잘 돼요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"경력 발전에 대한 방향성을 잃어서 현재 상황에 안주하고 있는 것 같아요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"업무 강도가 줄어든 시기에 여유롭게 일할 수 있어서 스트레스가 현저히 줄었어요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"같은 업무의 반복으로 인해 창의성이나 혁신적 사고가 둔화되고 있는 것 같아요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"휴가를 통해 완전히 업무에서 벗어나니 머릿속이 맑아지고 재충전되는 느낌이에요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"경제적으로 안정된 상황에서 돈에 대한 걱정 없이 여유롭게 생활할 수 있어서 평화로워요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"재테크나 투자에 대한 관심이 식어서 돈 관리를 소홀히 하고 있어요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"큰 지출 없이 소박하게 생활하니 마음의 부담이 줄어들고 만족스러워요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"경제 활동에 대한 의욕이 떨어져서 추가 수입을 늘리려는 노력을 하지 않고 있어요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"필수적인 소비만 하고 여유 자금은 저축하며 안정적으로 관리하고 있어요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"물질적 욕구가 줄어들어서 쇼핑이나 소비에 대한 관심이 많이 감소했어요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"가계부 정리를 통해 불필요한 지출을 줄이니 경제적 여유와 마음의 평화를 얻었어요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"경제적 목표나 계획 없이 현재 상황에 안주하며 살고 있어요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"경제적 부담을 줄이고 단순한 생활을 하니 스트레스가 현저히 감소했어요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"투자 수익에 대한 기대를 낮추고 안전한 상품 위주로 운용하며 마음의 안정을 찾았어요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"절약 생활을 통해 경제적 여유를 만들어가는 과정에서 소소한 만족감을 느껴요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"경제적 성공에 대한 욕심이 줄어들어서 현재 수준에서 만족하며 살고 있어요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"부채 없는 생활을 유지하며 경제적 부담감에서 해방된 자유로움을 만끽하고 있어요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"소비 패턴이 소극적으로 변해서 새로운 상품이나 서비스에 관심이 없어졌어요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"미니멀 라이프를 실천하며 물질보다는 경험과 관계에 가치를 두고 있어요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"명상을 통해 마음의 고요함을 찾고 내면의 평화로운 상태를 유지하고 있어요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"삶에 대한 열정이나 목표 의식이 예전만큼 강하지 않아서 무기력함을 느껴요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"자연과 함께하는 시간을 통해 내면의 안정감과 조화로움을 경험하고 있어요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"자기 성찰이나 발전에 대한 의욕이 떨어져서 현재 상태에 머물러 있어요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"깊은 호흡과 함께하는 이완 시간이 몸과 마음의 긴장을 완전히 풀어줘요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"감정의 기복이 줄어들어서 평온하지만 때로는 무감각한 상태가 돼요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"일기 쓰기나 독서를 통해 내면과 소통하는 조용한 시간이 소중해요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"새로운 도전이나 변화에 대한 욕구가 줄어들어서 안정성을 추구하게 됐어요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"영성적인 활동이나 철학적 사색을 통해 마음의 깊이를 탐구하고 있어요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"감정적 에너지가 낮아져서 강렬한 희로애락을 경험하는 일이 줄어들었어요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"내면의 목소리에 귀 기울이며 자신과의 대화 시간을 늘리고 있어요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"삶의 의미나 목적에 대한 고민이 줄어들어서 그냥 흘러가는 대로 살고 있어요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"감사 명상이나 긍정적 사고 훈련을 통해 마음의 평정을 유지하려 노력해요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"개인적 성장이나 자아실현에 대한 관심이 예전만큼 크지 않아서 현재에 안주해요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"마음의 여유를 찾아가면서 급하지 않고 천천히 살아가는 방식을 택하고 있어요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"오랜 친구와 편안하게 수다떨며 보내는 시간이 세상에서 가장 자연스럽고 평화로워요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"인간관계"
    }
  },
  {
    "content":"사람들과의 관계에서 피로감을 느껴서 혼자 있는 시간을 더 선호하게 됐어요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"인간관계"
    }
  },
  {
    "content":"가족과 함께 아무 말 없이 TV를 보며 보내는 시간도 따뜻하고 안정감을 줘요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"인간관계"
    }
  },
  {
    "content":"새로운 사람들을 만날 의욕이 떨어져서 기존 관계에만 안주하고 있는 것 같아요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"인간관계"
    }
  },
  {
    "content":"연인과 함께 조용한 카페에서 대화하며 보내는 시간이 마음을 평온하게 해줘요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"인간관계"
    }
  },
  {
    "content":"인간관계에서 갈등을 피하려고 하다 보니 관계가 깊어지지 못하고 표면적으로 머물러요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"인간관계"
    }
  },
  {
    "content":"친구들과의 모임에서 부담 없이 웃고 떠드는 시간이 스트레스를 완전히 날려 보내줘요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"인간관계"
    }
  },
  {
    "content":"사회적 활동에 참여하는 것이 귀찮아져서 집에만 있으려는 경향이 강해졌어요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"인간관계"
    }
  },
  {
    "content":"가족들과 함께 식사하며 일상적인 대화를 나누는 시간이 가장 편안하고 자연스러워요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"인간관계"
    }
  },
  {
    "content":"인간관계를 유지하는 것에 에너지가 부족해서 연락을 자주 하지 않게 됐어요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"인간관계"
    }
  },
  {
    "content":"반려동물과 함께 조용히 시간을 보내는 것이 사람과의 관계보다 편안하게 느껴져요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"인간관계"
    }
  },
  {
    "content":"깊이 있는 대화나 감정적 교류보다는 가벼운 만남을 선호하게 됐어요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"인간관계"
    }
  },
  {
    "content":"배우자와 함께 아무 계획 없이 여유롭게 보내는 주말이 가장 행복한 시간이에요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"인간관계"
    }
  },
  {
    "content":"사람들과의 만남에서 의미나 목적을 찾지 못해서 관계가 소원해지고 있어요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"인간관계"
    }
  },
  {
    "content":"조용한 공간에서 소수의 친한 사람들과 보내는 시간이 대규모 모임보다 편해요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"인간관계"
    }
  },
  {
    "content":"생일을 조용하게 가족들과만 보내니 부담 없고 편안한 하루가 됐어요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"중요한 행사를 앞두고도 별다른 긴장감이나 설렘을 느끼지 못하고 있어요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"휴가철에 집에서 여유롭게 쉬며 보내는 시간이 어떤 여행보다도 힐링이 돼요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"명절이나 기념일에 대해 예전만큼 특별한 의미를 느끼지 못하게 됐어요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"결혼 기념일을 소박하게 집에서 보내니 진정한 행복의 의미를 다시 생각하게 돼요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"새해가 와도 새로운 계획이나 목표에 대한 의욕이 크게 생기지 않아요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"가족 모임을 간소하게 진행하니 모든 구성원이 편안해하고 만족스러워해요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"특별한 날에도 평상시와 다름없이 지내는 것이 오히려 스트레스가 없어서 좋아요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"졸업식이나 입학식 같은 의식적인 행사에서 담담하고 평온한 마음으로 참여해요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"중요한 발표나 행사를 앞두고도 크게 준비하거나 긴장하지 않게 됐어요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"연말연시를 조용히 보내며 한 해를 돌아보는 시간이 의미 있게 느껴져요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"특별한 이벤트보다는 일상의 소소한 행복을 더 소중하게 여기게 됐어요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"기념일이나 축제에 대한 관심이 줄어들어서 평범한 일상을 더 선호해요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"큰 행사나 모임에 참여하기보다는 조용한 개인 시간을 갖는 것을 좋아해요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"특별한 날의 의미보다는 매일매일의 평범한 순간들에서 가치를 찾고 있어요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"창작 과정에서 느끼는 평온함과 몰입감이 마음에 깊은 안정을 가져다줘요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"창작에 대한 열정이 예전만큼 강하지 않아서 작품 활동이 소극적이 됐어요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"자연스럽게 흘러나오는 영감을 따라 부담 없이 창작하는 시간이 치유적이에요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"새로운 기법이나 장르에 도전할 의욕이 떨어져서 익숙한 방식만 고수하고 있어요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"창작을 통한 명상적 경험이 마음의 평화와 내적 안정감을 가져다줘요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"작품 완성에 대한 압박감 없이 과정 자체를 즐기며 여유롭게 작업하고 있어요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"창작 활동의 강도가 줄어들어서 예전만큼 활발하게 작품을 만들지 않고 있어요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"예술적 표현을 통해 내면의 고요함과 평온함을 표현하는 작업을 선호해요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"창작에 대한 야심이나 목표 의식이 줄어들어서 취미 수준에서 즐기고 있어요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"자연이나 일상의 소소한 아름다움을 담는 잔잔한 작품 활동에 집중하고 있어요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"창작 모임이나 전시 참여에 대한 관심이 줄어들어서 개인적으로만 작업해요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"기존 작품을 다시 보며 감상하는 시간이 새로운 작품을 만드는 것보다 의미 있어요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"창작을 통한 자기표현보다는 마음의 정화와 치유에 중점을 두고 있어요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"완벽한 작품을 만들어야 한다는 부담에서 벗어나 자유롭게 표현하고 있어요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"창작 속도가 느려져도 조급해하지 않고 자연스러운 리듬을 따라가고 있어요.",
    "metadata":{
      "emotion":"이완과 침체",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"새로운 동네로 이사 온 후 길을 잃고 헤매면서 방향감각을 잃어 혼란스러워요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"너무 많은 취미 옵션 앞에서 어떤 것을 선택해야 할지 결정하지 못하고 있어요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"여행 계획을 세우는데 정보가 너무 많아서 무엇이 맞는 정보인지 헷갈려요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"요리 레시피를 따라 하는데 설명이 애매해서 제대로 하고 있는지 의심스러워요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"가전제품 사용법이 복잡해서 매뉴얼을 봐도 이해가 안 되고 답답해요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"운동 방법이 너무 다양해서 내게 맞는 운동이 무엇인지 확신이 서지 않아요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"집 인테리어를 바꾸려는데 스타일이 너무 많아서 어떤 방향으로 할지 갈피를 못 잡겠어요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"반려동물이 보이는 행동이 정상인지 아닌지 판단하기 어려워서 걱정돼요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"친구들이 추천한 영화나 책들 중에서 무엇부터 봐야 할지 우선순위를 정하지 못하겠어요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"일상 루틴을 바꾸고 싶은데 어떻게 시작해야 할지 방법을 찾지 못하고 있어요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"쇼핑할 때 비슷한 상품들 사이에서 어떤 것이 더 나은지 결정하기 어려워요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"주말 계획을 세우려는데 하고 싶은 일이 너무 많아서 무엇을 선택할지 혼란스러워요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"새로운 지역의 교통수단을 이용할 때 노선이 복잡해서 어디로 가야 할지 모르겠어요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"건강한 식단에 대한 정보들이 상충되어서 무엇을 믿고 따라야 할지 의문이 들어요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"여가 시간을 의미 있게 보내고 싶은데 무엇이 진짜 의미 있는 활동인지 확신이 없어요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"몸에 나타나는 증상이 심각한 것인지 일시적인 것인지 판단하기 어려워요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"의사마다 다른 진단을 내려서 누구의 말을 믿어야 할지 혼란스러워요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"건강 정보가 너무 많고 상충되어서 무엇이 정확한 정보인지 확신이 없어요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"새로운 약물을 처방받았는데 부작용이 걱정되어서 복용해야 할지 망설여져요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"운동 후 몸의 변화가 좋은 것인지 나쁜 것인지 구분하기 어려워요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"다이어트 방법이 너무 다양해서 어떤 것이 내게 맞는지 선택하기 힘들어요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"건강검진 결과를 해석하는 과정에서 전문 용어들이 이해되지 않아 답답해요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"정신적 스트레스가 신체에 미치는 영향인지 실제 질병인지 구분이 안 돼요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"보완 대체의학과 현대의학 중 어떤 것을 선택해야 할지 갈등이 생겨요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"가족력과 개인적 위험도 사이에서 어느 정도까지 걱정해야 할지 모르겠어요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"건강 관련 온라인 정보가 너무 많아서 신뢰할 만한 것을 구별하기 어려워요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"병원 진료를 받아야 할 타이밍을 정하기 어려워서 계속 미루고 있어요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"치료 방법의 선택지가 여러 개 있어서 어떤 것이 최선인지 결정하기 힘들어요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"건강 상태에 대한 가족들의 의견이 달라서 누구의 조언을 따라야 할지 고민돼요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"예방의학적 조치들이 정말 효과적인지 과연 필요한 것인지 의문이 들어요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"새로운 앱을 사용하는데 기능이 복잡해서 제대로 활용하고 있는지 확신이 없어요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"온라인에서 받은 정보가 사실인지 가짜인지 구별하기 어려워서 혼란스러워요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"SNS에서 보는 다른 사람들의 삶이 진실인지 과장된 것인지 의심하게 돼요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"개인정보 보호 설정이 복잡해서 제대로 설정했는지 확신이 서지 않아요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"온라인 쇼핑에서 판매자의 신뢰도를 판단하기 어려워서 구매를 망설이게 돼요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"디지털 기기의 새로운 기능들이 너무 많아서 어떤 것들이 유용한지 모르겠어요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"온라인 교육 플랫폼이 너무 다양해서 어떤 것을 선택해야 할지 결정하기 힘들어요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"클라우드 서비스를 사용하는데 보안이 정말 안전한지 의심스러워요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"소셜미디어 알고리즘이 보여주는 콘텐츠가 편향된 것은 아닌지 걱정돼요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"온라인 리뷰들이 조작된 것인지 진짜인지 구분하기 어려워요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"디지털 결제 시스템을 사용할 때 해킹이나 사기 위험은 없는지 불안해요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"인터넷에서 찾은 정보의 신뢰성을 어떻게 검증해야 할지 방법을 모르겠어요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"온라인 게임에서 다른 플레이어들의 정체성이 진짜인지 확실하지 않아요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"디지털 광고와 실제 콘텐츠를 구별하기 어려워서 무엇을 믿어야 할지 모르겠어요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"새로운 온라인 서비스를 이용할 때 약관이 복잡해서 무엇에 동의하는 건지 헷갈려요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"새로운 프로젝트의 요구사항이 명확하지 않아서 어떻게 진행해야 할지 혼란스러워요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"상사의 지시가 애매해서 정확히 무엇을 원하는지 이해하지 못하고 있어요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"학습할 분야가 너무 방대해서 어디서부터 시작해야 할지 감이 잡히지 않아요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"동료들의 조언이 서로 다르다 보니 누구의 말을 따라야 할지 판단하기 어려워요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"새로운 업무 시스템이 복잡해서 제대로 사용하고 있는지 확신이 서지 않아요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"온라인 강의 내용이 이해되지 않아서 내가 제대로 따라가고 있는지 의심스러워요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"승진이나 이직을 고민하는데 어떤 선택이 더 나은지 결정하지 못하고 있어요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"업무 우선순위를 정하는 것이 어려워서 무엇부터 처리해야 할지 갈피를 못 잡겠어요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"새로운 기술을 배우는데 너무 어려워서 내가 이 분야에 적합한지 의문이 들어요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"팀 프로젝트에서 내 역할이 명확하지 않아서 무엇을 해야 할지 혼란스러워요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"경력 개발 방향에 대해 여러 의견을 들으니 어떤 길이 맞는지 확신이 없어요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"업무 성과를 평가받을 때 기준이 모호해서 잘하고 있는지 판단하기 어려워요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"새로운 직장 문화에 적응하는 과정에서 어떻게 행동해야 할지 갈등이 생겨요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"전문 자격증 취득을 고민하는데 정말 필요한 것인지 확신이 서지 않아요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"업무와 학습의 균형을 맞추는 것이 어려워서 시간 배분을 어떻게 해야 할지 모르겠어요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"투자 상품이 너무 다양해서 어떤 것을 선택해야 할지 결정하기 어려워요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"경제 뉴스에서 상반된 전망을 제시해서 미래를 예측하기 힘들고 혼란스러워요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"대출 조건들이 복잡해서 어떤 것이 더 유리한지 비교하기 어려워요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"보험 상품의 설명이 복잡해서 정말 필요한 보장인지 판단하기 힘들어요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"부동산 투자를 고민하는데 전문가들의 의견이 달라서 혼란스러워요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"가계부를 정리해봐도 돈이 어디로 나가는지 파악하기 어려워요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"온라인 쇼핑에서 리뷰가 엇갈려서 제품이 정말 좋은 것인지 의심스러워요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"신용카드 혜택이 복잡해서 어떤 카드를 사용하는 것이 유리한지 모르겠어요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"적금과 펀드 중에서 어떤 것이 더 나은 선택인지 확신이 서지 않아요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"할인 혜택의 조건이 복잡해서 정말 저렴한 것인지 계산하기 어려워요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"경제적 목표를 세우려는데 현실적인 기준을 잡기 어려워서 갈피를 못 잡겠어요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"재테크 정보가 너무 많아서 어떤 것을 믿고 따라야 할지 선택하기 힘들어요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"가족의 경제적 의사결정에서 내 의견이 맞는지 확신이 없어요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"소비 패턴을 바꾸려는데 어떤 방향이 올바른 것인지 기준을 세우기 어려워요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"경제적 안정과 위험 투자 사이에서 어떤 비율로 배분해야 할지 모르겠어요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"내가 정말 원하는 것이 무엇인지 확신이 서지 않아서 결정을 내리기 어려워요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"감정의 변화가 심해서 진짜 내 마음이 어떤 것인지 파악하기 힘들어요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"과거의 선택들이 옳았는지 잘못됐는지 계속 의심하게 돼요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"다른 사람들의 조언이 너무 다양해서 무엇을 따라야 할지 갈피를 못 잡겠어요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"내 성격이나 정체성에 대해 확신이 없어서 자아 정체감이 혼란스러워요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"인생의 방향이나 목표에 대해 계속 의문이 들어서 확신을 갖지 못하겠어요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"내가 느끼는 감정이 정당한 것인지 과도한 것인지 판단하기 어려워요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"자신에 대한 평가가 객관적인 것인지 주관적인 것인지 구분이 안 돼요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"가치관이나 신념에 대해 흔들리는 순간들이 있어서 혼란스러워요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"내면의 목소리와 외부의 기대 사이에서 어떤 것을 따라야 할지 갈등이 생겨요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"감정을 표현하는 방식이 적절한지 아닌지 확신이 서지 않아요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"스스로에 대한 기대 수준을 어떻게 설정해야 할지 기준을 잡기 어려워요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"내가 추구하는 행복의 정의가 올바른 것인지 의문이 들어요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"과거의 상처나 트라우마가 현재에 미치는 영향을 정확히 파악하기 어려워요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"자기 성찰의 결과를 해석하는 과정에서 객관성을 유지하기 힘들어요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"친구의 말과 행동이 일치하지 않아서 진심인지 의심하게 돼요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"인간관계"
    }
  },
  {
    "content":"새로운 사람을 만났는데 첫인상과 다른 면을 보여서 어떤 사람인지 혼란스러워요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"인간관계"
    }
  },
  {
    "content":"연인의 태도가 갑자기 변해서 우리 관계에 문제가 있는지 의심하고 있어요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"인간관계"
    }
  },
  {
    "content":"가족 간의 갈등 상황에서 누구 편을 들어야 할지 판단하기 어려워요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"인간관계"
    }
  },
  {
    "content":"직장 동료의 의도를 파악하기 어려워서 협력해야 할지 경계해야 할지 고민돼요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"인간관계"
    }
  },
  {
    "content":"친구들 사이의 모임에서 내가 끼어있는 건지 소외되는 건지 확신이 없어요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"인간관계"
    }
  },
  {
    "content":"상대방이 보내는 신호가 애매해서 관심이 있는 건지 없는 건지 헷갈려요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"인간관계"
    }
  },
  {
    "content":"SNS에서 보는 지인들의 모습이 진짜인지 가짜인지 의심하게 돼요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"인간관계"
    }
  },
  {
    "content":"새로운 환경에서 사람들과 어떻게 관계를 맺어야 할지 방법을 모르겠어요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"인간관계"
    }
  },
  {
    "content":"친구의 조언이 정말 나를 위한 것인지 다른 의도가 있는 건지 의심스러워요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"인간관계"
    }
  },
  {
    "content":"가족의 간섭이 사랑인지 통제인지 구분하기 어려워서 혼란스러워요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"인간관계"
    }
  },
  {
    "content":"연인과의 미래에 대해 서로 다른 기대를 갖고 있어서 관계가 불확실해요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"인간관계"
    }
  },
  {
    "content":"인간관계에서 진심과 겉치레를 구별하기 어려워서 누구를 믿어야 할지 모르겠어요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"인간관계"
    }
  },
  {
    "content":"갈등 상황에서 화해를 시도해야 할지 거리를 두어야 할지 판단이 안 서요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"인간관계"
    }
  },
  {
    "content":"사회적 모임에서 어떻게 행동해야 적절한지 기준을 잡기 어려워요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"인간관계"
    }
  },
  {
    "content":"결혼 준비 과정에서 선택해야 할 것들이 너무 많아서 무엇이 중요한지 갈피를 못 잡겠어요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"중요한 시험을 앞두고 준비 방향이 맞는지 확신이 서지 않아서 불안해요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"취업 면접에서 어떤 답변이 좋은 인상을 줄지 예측하기 어려워요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"가족 행사를 준비하는데 전통과 현대적 방식 중 어떤 것을 선택할지 고민돼요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"이사할 지역을 정하는데 고려 사항이 너무 많아서 최선의 선택이 무엇인지 모르겠어요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"졸업 후 진로를 결정해야 하는데 여러 선택지 앞에서 혼란스러워요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"생일 파티 계획을 세우는데 어떤 스타일이 좋을지 결정하기 어려워요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"새로운 직장의 첫 출근을 앞두고 어떻게 준비해야 할지 방향을 잡기 힘들어요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"중요한 발표를 앞두고 내용 구성을 어떻게 해야 할지 확신이 없어요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"여행 일정을 짜는데 가보고 싶은 곳이 너무 많아서 우선순위를 정하기 어려워요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"입학 준비 과정에서 어떤 것들을 우선적으로 해야 할지 순서를 정하지 못하겠어요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"새해 계획을 세우려는데 현실적으로 달성 가능한 목표인지 판단하기 어려워요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"기념일 선물을 준비하는데 상대방이 정말 좋아할지 확신이 서지 않아요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"중요한 결정을 내려야 하는 시점에서 장단점을 따져봐도 답이 명확하지 않아요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"특별한 행사의 규모나 형식을 정하는데 적절한 수준이 어느 정도인지 모르겠어요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"내 작품의 방향성이 맞는지 확신이 서지 않아서 계속 수정하게 돼요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"창작 기법들이 너무 다양해서 어떤 것을 선택해야 할지 결정하기 어려워요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"다른 창작자들의 작품을 보면 내 수준이 어느 정도인지 객관적으로 판단하기 힘들어요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"창작 동기가 순수한 것인지 아니면 인정받고 싶은 욕구인지 구별이 안 돼요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"비평이나 피드백을 받을 때 어떤 것이 건설적인 조언인지 판단하기 어려워요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"새로운 장르에 도전할 때 내가 그 분야에 적합한지 확신이 없어요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"창작 과정에서 나오는 아이디어가 독창적인지 아니면 어디선가 본 것인지 헷갈려요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"작품의 완성도를 평가하는 기준을 어떻게 세워야 할지 갈피를 못 잡겠어요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"상업적 성공과 예술적 가치 사이에서 어떤 것을 우선해야 할지 고민돼요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"창작 교육을 받을 때 선생님마다 다른 방법을 제시해서 혼란스러워요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"내가 추구하는 예술적 목표가 현실적으로 달성 가능한지 의문이 들어요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"창작 활동을 지속해야 할지 다른 길을 모색해야 할지 확신이 서지 않아요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"영감의 원천이 진정한 것인지 일시적인 감정인지 구분하기 어려워요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"작품에 대한 자신의 만족도와 타인의 평가가 다를 때 어떤 것을 믿어야 할지 모르겠어요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"창작자로서의 성장 방향을 설정하는데 너무 많은 선택지가 있어서 혼란스러워요.",
    "metadata":{
      "emotion":"혼란과 의심",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"일출을 보면서 자연의 장엄함에 경이로움을 느끼고 하루를 시작하게 돼요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"집안일이 너무 많이 쌓여서 어디서부터 시작해야 할지 압도당하는 기분이에요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"산 정상에서 바라본 광활한 풍경이 너무 아름다워서 말문이 막혀요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"새로운 취미를 시작하려고 하는데 배워야 할 것들이 너무 많아서 벅차요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"밤하늘의 별을 보면서 우주의 무한함 앞에서 인간의 작음을 느끼고 경외감이 들어요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"정리해야 할 물건들이 너무 많아서 정리 자체가 부담스럽고 압도돼요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"꽃이 피어나는 과정을 보면서 생명의 신비로움에 깊은 감동을 받아요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"여행 계획을 세우는데 가보고 싶은 곳과 해야 할 일들이 너무 많아서 혼란스러워요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"거대한 폭포 앞에 서니 자연의 웅장함에 압도되어 한동안 넋을 잃고 바라봤어요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"새로운 요리법을 시도하려는데 재료와 과정이 복잡해서 시작하기 전부터 지쳐요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"아침 이슬이 맺힌 거미줄을 보면서 자연 속 작은 예술품에 경탄하게 돼요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"반려동물을 돌보는 일이 생각보다 책임과 일이 많아서 때때로 벅찬 기분이 들어요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"오케스트라 연주를 들으면서 음악의 웅장함과 아름다움에 온몸이 전율해요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"집 전체를 대청소하려니 규모가 너무 커서 어디서부터 손을 대야 할지 막막해요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"우연히 본 무지개의 선명한 색깔에 자연의 마법 같은 아름다움을 느꼈어요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"일상 및 여가"
    }
  },
  {
    "content":"인간 몸의 정교한 시스템과 자가 치유 능력을 알게 되면서 생명의 신비로움에 경탄해요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"건강 관리를 위해 신경 써야 할 것들이 너무 많아서 무엇부터 시작해야 할지 막막해요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"의학 기술의 발전과 수술의 정밀함을 보면서 현대 의학의 놀라움을 느껴요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"만성 질환 관리에 필요한 생활 습관 변화들이 너무 많아서 실천하기 벅차요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"운동선수의 신체 능력과 한계 극복 정신을 보며 인간 잠재력에 감탄하게 돼요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"건강검진 결과와 각종 수치들을 이해하고 관리하는 것이 생각보다 복잡하고 어려워요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"임신과 출산 과정에서 일어나는 생명 탄생의 기적에 경외감과 감동을 느껴요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"여러 전문의들의 다양한 조언과 치료 방법들 중에서 선택하는 것이 부담스러워요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"뇌과학 연구 결과들을 접하면서 인간 의식과 뇌의 복잡함에 놀라워해요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"가족의 건강 상태 변화에 따라 돌봄의 책임이 커져서 감당하기 어려울 때가 있어요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"재활 치료 과정에서 보이는 인간의 회복 의지와 적응력에 깊은 감명을 받아요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"건강한 생활을 위한 정보들이 너무 많고 복잡해서 실제로 적용하기 힘들어요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"의료진의 전문성과 헌신적인 치료 노력을 보면서 의학의 숭고함을 느껴요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"노화 과정과 그에 따른 변화들을 받아들이고 관리하는 것이 예상보다 어려워요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"정신건강 관리의 중요성과 복잡성을 깨달으면서 마음의 섬세함에 경이로워해요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"건강 및 의료"
    }
  },
  {
    "content":"인공지능 기술의 발전 속도와 능력을 보면서 기술 혁신의 놀라움에 경탄해요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"관리해야 할 온라인 계정과 플랫폼들이 너무 많아서 모든 것을 체크하기 벅차요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"가상현실이나 메타버스 기술을 체험하면서 디지털 세계의 무한한 가능성에 경이로워해요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"매일 쏟아지는 디지털 정보의 양이 너무 방대해서 선별하고 처리하기 어려워요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"프로그래머들의 복잡한 코딩 능력과 창의적 해결책을 보면서 기술적 재능에 감탄해요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"SNS, 이메일, 메신저 등에서 오는 알림들이 너무 많아서 모두 확인하기 힘들어요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"빅데이터 분석과 패턴 인식 기술을 보면서 데이터 과학의 힘에 놀라워해요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"디지털 보안 관리, 개인정보 보호 등 신경 써야 할 것들이 너무 많아서 부담스러워요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"온라인 교육 플랫폼의 무한한 학습 자원을 보면서 지식 접근성의 혁명에 경탄해요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"여러 디지털 기기와 앱들을 동기화하고 관리하는 것이 생각보다 복잡하고 어려워요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"크리에이터들의 창의적인 콘텐츠와 기술 활용을 보면서 디지털 예술에 감탄해요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"온라인에서 받는 각종 광고, 스팸, 정보들을 필터링하는 것이 압도적으로 번거로워요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"블록체인과 암호화폐 기술의 혁신성을 보면서 금융 기술의 미래에 경외감을 느껴요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"각종 앱의 업데이트와 새로운 기능들을 따라가는 것이 부담스럽고 피곤해요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"IoT와 스마트홈 기술을 보면서 연결된 세상의 편리함과 복잡성에 놀라워해요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"디지털 및 온라인 활동"
    }
  },
  {
    "content":"새로운 프로젝트의 규모와 복잡성을 보니 성공적으로 완수할 수 있을지 압도돼요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"동료의 뛰어난 프레젠테이션을 보고 그 전문성과 실력에 깊은 감탄을 했어요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"배워야 할 새로운 기술의 범위가 너무 방대해서 어디서부터 시작해야 할지 막막해요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"멘토의 깊은 지혜와 통찰력에 항상 경이로움을 느끼고 많은 것을 배우고 있어요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"업무량이 급격히 늘어나서 모든 것을 처리하기에는 너무 벅차고 부담스러워요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"인공지능 기술의 발전 속도와 가능성을 보면서 미래에 대한 경외감을 느껴요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"새로운 직무에 필요한 역량들이 너무 많아서 습득하기까지 오랜 시간이 걸릴 것 같아요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"업계 리더의 강연을 들으면서 그들의 비전과 성취에 깊은 감명을 받았어요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"동시에 진행해야 하는 여러 프로젝트들 때문에 시간 관리가 압도적으로 어려워요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"전문 분야의 깊이 있는 지식을 접할 때마다 학문의 광대함에 경탄하게 돼요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"신입사원 교육 프로그램이 너무 집약적이어서 모든 내용을 소화하기 힘들어요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"천재적인 동료의 문제 해결 능력을 보면서 인간 지성의 놀라움을 느껴요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"마감일이 임박한 과제들이 산더미처럼 쌓여서 우선순위를 정하는 것조차 어려워요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"학회에서 발표된 혁신적인 연구 결과들을 보며 과학 발전의 속도에 놀라워요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"새로운 시스템 도입으로 변화하는 업무 환경에 적응하는 것이 생각보다 버거워요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"업무 및 학습"
    }
  },
  {
    "content":"글로벌 경제 시스템의 복잡함과 상호 연결성을 보면서 현대 사회의 정교함에 감탄해요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"가계 관리에 필요한 여러 요소들을 동시에 고려하는 것이 생각보다 복잡하고 어려워요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"성공한 기업가의 비전과 경영 철학을 들으면서 비즈니스 통찰력에 경외감을 느껴요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"투자 상품의 종류와 조건들이 너무 다양해서 모든 것을 이해하기 벅차요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"기술 혁신이 경제에 미치는 파급효과를 보면서 변화의 속도에 놀라워해요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"재정 계획을 세우는데 고려해야 할 변수들이 너무 많아서 압도당하는 기분이에요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"경제학자들의 깊이 있는 분석과 예측 능력을 보며 학문적 통찰력에 감탄해요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"부동산, 주식, 보험 등 관리해야 할 자산들이 많아져서 감당하기 어려워요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"암호화폐와 블록체인 기술의 혁신성을 보면서 금융 패러다임 변화에 경이로워해요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"가족의 교육비, 의료비, 노후 자금 등을 동시에 준비하는 것이 부담스러워요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"대기업 CEO들의 경영 전략과 리더십을 보면서 조직 운영의 예술성에 감탄해요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"경제 위기 상황에서 대응해야 할 일들이 너무 많아서 우선순위를 정하기 어려워요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"사회적 기업의 지속가능한 비즈니스 모델을 보며 경제와 사회적 가치의 조화에 놀라워요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"세금, 보험, 투자 수익률 등을 모두 계산하며 재정 관리하는 것이 복잡해요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"경제 지표들의 상호 작용과 시장 변동성을 보면서 경제 시스템의 역동성에 경탄해요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"경제 및 소비생활"
    }
  },
  {
    "content":"명상을 통해 의식의 깊이와 내면 세계의 광활함을 경험하며 경이로움을 느껴요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"동시에 일어나는 여러 감정들을 모두 이해하고 처리하는 것이 감정적으로 벅차요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"인간 정신의 복잡성과 무의식의 깊이를 탐구하면서 마음의 신비로움에 감탄해요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"해결해야 할 내면의 갈등들과 성장 과제들이 너무 많아서 어디서부터 시작할지 막막해요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"철학자들의 깊은 사상과 통찰을 접하면서 인간 사고의 무한함에 경외감을 느껴요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"자기 성찰 과정에서 발견하는 내 모습들이 너무 다양하고 복잡해서 정리하기 어려워요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"예술작품이나 음악에서 느끼는 깊은 감동과 영적 체험에 말할 수 없는 경이로움을 느껴요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"변화하고 싶은 부분들과 개선해야 할 습관들이 너무 많아서 감당하기 힘들어요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"꿈의 상징성과 무의식의 메시지를 해석하면서 정신세계의 신비로움에 놀라워해요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"감정 조절, 스트레스 관리, 대인관계 등 신경 써야 할 정신건강 요소들이 복잡해요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"종교적 체험이나 영성적 깨달음의 순간에 우주와의 연결감에 깊은 경외감을 느껴요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"내면의 다양한 목소리들과 상충하는 욕구들 사이에서 균형을 찾는 것이 어려워요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"인간 의식의 신비로움과 자아 정체성의 복잡함을 탐구하면서 존재에 대해 경탄해요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"성격 개발, 가치관 정립, 인생 목표 설정 등 해야 할 내적 작업들이 부담스러워요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"타인의 내면 세계와 감정의 깊이를 이해하게 될 때 인간성의 아름다움에 감동받아요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"내면 활동 및 감정"
    }
  },
  {
    "content":"친구의 극한 상황에서도 흔들리지 않는 의지력을 보며 인간 정신의 강인함에 감탄해요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"인간관계"
    }
  },
  {
    "content":"여러 사람들과의 관계를 동시에 관리하는 것이 생각보다 복잡하고 에너지가 많이 들어요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"인간관계"
    }
  },
  {
    "content":"부모님의 무조건적인 사랑과 헌신을 새삼 깨달으며 그 크기에 경외감을 느껴요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"인간관계"
    }
  },
  {
    "content":"사회적 모임에서 다양한 사람들과 대화해야 하는 상황이 때로는 압도적으로 느껴져요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"인간관계"
    }
  },
  {
    "content":"연인의 깊은 이해심과 배려에 매번 감동하며 사랑의 놀라운 힘을 경험해요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"인간관계"
    }
  },
  {
    "content":"인간관계에서 발생하는 여러 갈등들을 해결하는 것이 예상보다 복잡하고 어려워요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"인간관계"
    }
  },
  {
    "content":"할머니의 인생 경험과 지혜에서 나오는 조언들에 항상 깊은 감탄을 하게 돼요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"인간관계"
    }
  },
  {
    "content":"새로운 환경에서 만나는 사람들과 관계를 형성해야 하는 부담감이 벅차게 느껴져요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"인간관계"
    }
  },
  {
    "content":"아이의 순수함과 무한한 상상력을 보면서 인간 본성의 아름다움에 경이로워해요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"인간관계"
    }
  },
  {
    "content":"가족 구성원 각자의 요구와 기대를 모두 만족시키려니 감정적으로 고갈되는 기분이에요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"인간관계"
    }
  },
  {
    "content":"친구가 어려운 상황을 극복하는 모습을 보며 인간의 회복력에 놀라움을 감추지 못해요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"인간관계"
    }
  },
  {
    "content":"직장에서의 인간관계와 사적인 관계를 균형 있게 유지하는 것이 생각보다 까다로워요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"인간관계"
    }
  },
  {
    "content":"멘토의 인격적 완성도와 리더십을 보면서 인간적 성장의 가능성에 감탄해요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"인간관계"
    }
  },
  {
    "content":"여러 세대가 함께하는 가족 모임에서 각기 다른 관점들을 조율하는 것이 복잡해요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"인간관계"
    }
  },
  {
    "content":"타인을 향한 무조건적 봉사와 헌신을 보면서 인간애의 숭고함에 마음이 뭉클해져요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"인간관계"
    }
  },
  {
    "content":"결혼식에서 느끼는 사랑의 숭고함과 평생의 약속에 경외감과 감동을 받아요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"중요한 행사 준비에 필요한 세부 사항들이 너무 많아서 관리하기 벅차요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"졸업식에서 그동안의 성장과 성취를 돌아보며 시간의 의미에 깊은 감회를 느껴요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"가족 결혼식, 돌잔치, 회갑연 등이 연달아 있어서 준비와 참석이 부담스러워요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"올림픽 같은 국제 행사에서 인간의 한계 도전 정신을 보며 경이로움을 느껴요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"새해 계획과 목표들을 세우는데 이루고 싶은 것들이 너무 많아서 정리하기 어려워요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"아이의 탄생 순간을 목격하면서 생명 탄생의 기적에 말로 표현할 수 없는 감동을 받아요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"여러 중요한 행사들이 겹쳐서 각각에 필요한 준비와 마음가짐을 갖추기 힘들어요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"역사적인 현장이나 유적지에서 느끼는 시간의 무게와 인류 문명에 경탄하게 돼요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"취업 준비 과정에서 해야 할 일들이 산더미처럼 쌓여서 어디서부터 시작할지 막막해요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"자연재해 후 보여주는 인간의 연대와 복구 의지를 보며 공동체 정신에 감동받아요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"이사하면서 정리해야 할 물건들과 처리할 일들이 너무 많아서 압도당해요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"문화 축제나 예술 공연에서 인간 창조력의 아름다움과 다양성에 경이로워해요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"동시에 여러 중요한 결정을 내려야 하는 시기에 부담감과 책임감이 벅차요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"인생의 전환점에서 느끼는 변화의 크기와 새로운 가능성에 경외감과 설렘을 느껴요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"특별한 날과 사건"
    }
  },
  {
    "content":"거장들의 예술 작품을 감상하면서 인간 창조력의 무한함과 아름다움에 경탄해요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"배워야 할 창작 기법들과 기술들이 너무 많아서 모든 것을 습득하기 벅차요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"자연에서 받는 영감과 창작 동기의 순간들에 예술의 신성함을 경험해요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"동시에 진행해야 하는 여러 창작 프로젝트들을 관리하는 것이 감당하기 어려워요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"천재 예술가들의 작품 세계와 독창성을 보면서 예술적 재능에 깊은 감탄을 해요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"창작 과정에서 극복해야 할 기술적, 정신적 장벽들이 너무 많아서 때로 좌절돼요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"음악, 문학, 미술 등에서 느끼는 숭고한 아름다움에 영혼이 정화되는 경험을 해요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"비평, 피드백, 자기 발전 등 신경 써야 할 성장 요소들이 복잡하고 부담스러워요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"창작을 통한 자기표현의 무한한 가능성을 발견하면서 예술의 힘에 경이로워해요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"완벽한 작품을 만들기 위해 고려해야 할 요소들이 너무 많아서 압도당하는 기분이에요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"다른 문화권의 예술과 창작 방식을 접하면서 인류 문화의 다양성에 감탄해요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"새로운 장르 도전, 기술 습득, 네트워킹 등 해야 할 일들이 산더미처럼 쌓여있어요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"창작 과정에서 일어나는 영감의 순간과 직감의 힘을 경험하며 무의식의 신비로움을 느껴요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"창작자로서 성장하기 위해 개발해야 할 능력들이 너무 다방면이어서 방향성을 잡기 어려워요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"창작과 성장"
    }
  },
  {
    "content":"예술이 사회와 개인에게 미치는 깊은 영향력을 보면서 창작의 책임감과 사명감에 경외감을 느껴요.",
    "metadata":{
      "emotion":"경이와 압도",
      "situation":"창작과 성장"
    }
  }
] 


QUOTES_DATA = [
  {
    "id": "advice_0",
    "document": "인생은 항상 공평하지 않을 수도 있어요. 그런 점을 이해하고 받아들이는 것이 중요합니다.",
    "metadata": {
      "author": "빌 게이츠",
      "authorProfile": "마이크로소프트 창업자",
      "message": "인생이란 결코 공평하지 않다. 이 사실에 익숙해져라."
    }
  },
  {
    "id": "advice_1",
    "document": "인생은 끔찍하고 비참한 순간들로 가득 차 있을 수 있어요.",
    "metadata": {
      "author": "우디 알렌",
      "authorProfile": "영화 감독",
      "message": "인생은 끔찍하거나 비참하거나 둘 중 하나다."
    }
  },
  {
    "id": "advice_2",
    "document": "내 인생은 내가 직접 바꿀 수 있어. 다른 사람이 대신 해줄 수는 없어.",
    "metadata": {
      "author": "캐롤 버넷",
      "authorProfile": "영화 배우",
      "message": "나만이 내 인생을 바꿀 수 있다. 아무도 날 대신해 해줄 수 없다."
    }
  },
  {
    "id": "advice_3",
    "document": "인생을 얼마나 오래 사는가보다 어떻게 잘 사는지가 더 중요해요.",
    "metadata": {
      "author": "벤자민 프랭클린",
      "authorProfile": "정치인, 미국 건국의 아버지",
      "message": "긴 인생은 충분히 좋지 않을 수 있다. 그러나 좋은 인생은 충분히 길다."
    }
  },
  {
    "id": "advice_4",
    "document": "인생은 가까이에서 보면 힘들 수 있지만, 멀리서 보면 웃을 수 있는 일도 많아요.",
    "metadata": {
      "author": "찰리 채플린",
      "authorProfile": "영화 배우",
      "message": "인생은 가까이서 보면 비극, 멀리서 보면 희극이다."
    }
  },
  {
    "id": "advice_5",
    "document": "반드시 이기지 않아도 괜찮지만, 진실해야 해. 꼭 성공하지 않더라도, 자신의 소신을 지키며 사는 게 중요해.",
    "metadata": {
      "author": "에이브러햄 링컨",
      "authorProfile": "미국 16대 대통령",
      "message": "반드시 이겨야 하는 건 아니지만 진실할 필요는 있다. 반드시 성공해야 하는 건 아니지만, 소신을 가지고 살아야 할 필요는 있다."
    }
  },
  {
    "id": "advice_6",
    "document": "삶을 살아가는 방법은 두 가지가 있습니다. 하나는 모든 것이 기적이라고 믿는 것이고, 다른 하나는 기적이 없다고 믿는 것입니다.",
    "metadata": {
      "author": "아인슈타인",
      "authorProfile": "물리학자, 상대성이론의 창시자",
      "message": "삶을 사는 방식에는 오직 두 가지가 있다. 하나는 모든 것을 기적이라고 믿는 것, 그리고 다른 하나는 기적은 없다고 믿는 것이다."
    }
  },
  {
    "id": "advice_7",
    "document": "지혜로운 사람일수록 시간을 헛되이 보내는 것을 아쉬워합니다.",
    "metadata": {
      "author": "단테",
      "authorProfile": "작가, 이탈리아어의 아버지",
      "message": "가장 지혜로운 자는 허송세월을 가장 슬퍼한다."
    }
  },
  {
    "id": "advice_8",
    "document": "어려움은 우리에게 강한 의지를 키워주고, 불행은 훌륭한 사람을 만든다.",
    "metadata": {
      "author": "빅토르 위고",
      "authorProfile": "작가, <레미제라블>의 저자",
      "message": "궁핍은 영혼과 정신을 낳고, 불행은 위대한 인물을 낳는다."
    }
  },
  {
    "id": "advice_9",
    "document": "우리 모두에게는 결점이 있지만, 그것을 인정하지 않는 것이 더 큰 문제일 수 있어요.",
    "metadata": {
      "author": "블레즈 파스칼",
      "authorProfile": "수학자, 계산기의 발명자",
      "message": "결점이 많다는 것은 나쁜 것이지만, 그것을 인정하지 않는 것은 더 나쁜 것이다."
    }
  },
  {
    "id": "advice_10",
    "document": "죽음보다 중요한 것은 어떻게 사느냐입니다. 죽음은 순식간에 지나가는 것이니까요.",
    "metadata": {
      "author": "제임스 보즈웰",
      "authorProfile": "작가",
      "message": "문제는 어떻게 죽느냐가 아니고 어떻게 사느냐이다. 죽음 자체는 중요하지 않다. 그것은 한순간의 일이다."
    }
  },
  {
    "id": "advice_11",
    "document": "살아가는 것은 조금씩 새롭게 태어나는 과정이에요.",
    "metadata": {
      "author": "생텍쥐페리",
      "authorProfile": "작가, <어린왕자>의 저자",
      "message": "산다는 것은 서서히 태어나는 것이다."
    }
  },
  {
    "id": "advice_12",
    "document": "살아 있는 졸병은 죽은 황제보다 더 소중합니다. 생명의 가치는 그 무엇과도 비교할 수 없어요.",
    "metadata": {
      "author": "나폴레옹",
      "authorProfile": "군인, 프랑스의 황제",
      "message": "살아 있는 졸병이 죽은 황제보다 훨씬 가치가 있다."
    }
  },
  {
    "id": "advice_13",
    "document": "인생은 자신을 발견하는 것이 아니라, 스스로 만들어가는 과정입니다.",
    "metadata": {
      "author": "롤리 다스칼",
      "authorProfile": "리더십 코치",
      "message": "인생이란 자신을 찾는 것이 아니라 자신을 만드는 것이다."
    }
  },
  {
    "id": "advice_14",
    "document": "좋아하지 않는 사람들에게 생각을 빼앗기지 마세요.",
    "metadata": {
      "author": "드와이트 아이젠하워",
      "authorProfile": "미국 34대 대통령",
      "message": "네가 좋아하지 않는 사람들을 생각하는데 단 1분도 허비하지 마라."
    }
  },
  {
    "id": "advice_15",
    "document": "오늘 하루가 소중한 이유는 어제 세상을 떠난 사람들이 그토록 바라던 내일이기 때문이에요.",
    "metadata": {
      "author": "소포클레스",
      "authorProfile": "극작가",
      "message": "당신이 헛되이 보낸 오늘은 어제 죽은 이가 그토록 갈망하던 내일이다."
    }
  },
  {
    "id": "advice_16",
    "document": "항상 열정을 잃지 말고 꾸준히 나아가세요.",
    "metadata": {
      "author": "스티브 잡스",
      "authorProfile": "애플 창업자",
      "message": "늘 갈망하고 우직하게 나아가라."
    }
  },
  {
    "id": "advice_17",
    "document": "자신의 삶을 되돌아보고 성찰하지 않으면, 진정한 의미를 찾기 어려울 수 있어요.",
    "metadata": {
      "author": "소크라테스",
      "authorProfile": "철학자",
      "message": "반성되지 않는 삶은 인간으로서 살 가치가 없다."
    }
  },
  {
    "id": "advice_18",
    "document": "삶을 이해하는 것도 어려운데, 죽음을 이해하는 건 더 어려울 수 있어요.",
    "metadata": {
      "author": "공자",
      "authorProfile": "유학자, 세계 4대 성인",
      "message": "삶도 모르는데 어찌 죽음을 알겠는가?"
    }
  },
  {
    "id": "advice_19",
    "document": "세상이 널 버렸다고 느끼지 마. 세상은 너를 소유한 적이 없었어.",
    "metadata": {
      "author": "에르빈 롬멜",
      "authorProfile": "독일의 장군, 사막의 여우",
      "message": "세상이 널 버렸다고 생각하지마라. 세상은 널 가진 적이 없다."
    }
  },
  {
    "id": "advice_20",
    "document": "시간은 돈과 같이 소중한 자원이니, 낭비하지 말고 가치 있게 사용해야 해요.",
    "metadata": {
      "author": "벤자민 프랭클린",
      "authorProfile": "정치인, 미국 건국의 아버지",
      "message": "시간은 돈이라는 사실을 명심하세요."
    }
  },
  {
    "id": "advice_21",
    "document": "언어의 범위가 곧 우리가 이해할 수 있는 세계의 범위예요.",
    "metadata": {
      "author": "루트비히 비트겐슈타인",
      "authorProfile": "철학자",
      "message": "언어의 한계가 곧 자기 세계의 한계다."
    }
  },
  {
    "id": "advice_22",
    "document": "인생은 계획이 아니라 실제로 살아가는 것이에요.",
    "metadata": {
      "author": "이상",
      "authorProfile": "작가",
      "message": "인생은 실험이 아니라 실행이다."
    }
  },
  {
    "id": "advice_23",
    "document": "사람의 가치는 부나 노동 여부로 결정되지 않아요. 모든 사람은 그 자체로 소중합니다.",
    "metadata": {
      "author": "레프 톨스토이",
      "authorProfile": "작가, 러시아의 대문호",
      "message": "일하지 않는 자나 부자나 가난한 자나 모두 쓸모있는 사람이다."
    }
  },
  {
    "id": "advice_24",
    "document": "불행의 원인은 대개 자신의 마음속에 있는 경우가 많습니다.",
    "metadata": {
      "author": "블레즈 파스칼",
      "authorProfile": "수학자, 계산기의 발명자",
      "message": "불행의 원인은 늘 자신에게 있다."
    }
  },
  {
    "id": "advice_25",
    "document": "과거에 얽매이지 말고, 미래를 바라보세요.",
    "metadata": {
      "author": "칼 힐티",
      "authorProfile": "사상가, 법률가",
      "message": "뒤돌아 보지 마라. 중요한 것은 미래다."
    }
  },
  {
    "id": "advice_26",
    "document": "사랑을 받는 것보다 사랑을 주는 사람이 되세요.",
    "metadata": {
      "author": "스탕달",
      "authorProfile": "작가",
      "message": "사랑 받기 보다는 사랑하는 사람이 되어라."
    }
  },
  {
    "id": "advice_27",
    "document": "인생에서 가장 중요한 것은 자신을 발견하는 것입니다.",
    "metadata": {
      "author": "프리드쇼프 난센",
      "authorProfile": "탐험가",
      "message": "인생에서 가장 중요한 일은 자기를 발견하는 것이다."
    }
  },
  {
    "id": "advice_28",
    "document": "괴물과 싸울 때는 스스로 괴물이 되지 않도록 주의해야 해요. 너무 오랫동안 어두운 곳을 바라보면, 그 어두움도 우리를 보고 있을 수 있어요.",
    "metadata": {
      "author": "프리드리히 니체",
      "authorProfile": "철학자",
      "message": "괴물과 싸우는 사람은 스스로 괴물이 되지 않도록 조심해야 한다. 우리가 괴물의 심연을 오래 들여다보면, 심연 또한 우리를 들여다 본다."
    }
  },
  {
    "id": "advice_29",
    "document": "타인의 의견에 너무 얽매이지 않아도 돼요. 당신의 현실은 당신이 만들어가니까요.",
    "metadata": {
      "author": "레스 브라운",
      "authorProfile": "동기부여 연설가",
      "message": "당신에 대한 누군가의 의견이 당신의 현실이 될 필요가 없다."
    }
  },
  {
    "id": "advice_30",
    "document": "자신감을 잃으면 세상이 나를 힘들게 할 수 있어요. 자신감을 가지세요!",
    "metadata": {
      "author": "랄프 왈도 에머슨",
      "authorProfile": "사상가, 시인",
      "message": "나 자신에 대한 자신감을 잃으면 온 세상이 나의 적이 된다."
    }
  },
  {
    "id": "advice_31",
    "document": "인생의 중요한 선택은 타인의 말에 휘둘리지 말고 스스로 내려야 해요.",
    "metadata": {
      "author": "은하철도 999",
      "authorProfile": "-",
      "message": "인생의 선택에 타인의 말은 필요없어!"
    }
  },
  {
    "id": "advice_32",
    "document": "신발이 없어 불평했지만, 발이 없는 사람을 보고 감사함을 느꼈어요.",
    "metadata": {
      "author": "데일 카네기",
      "authorProfile": "작가, 최초 자기계발서의 저자",
      "message": "나는 신발이 없음을 한탄했는데, 거리에서 발이 없는 사람을 만났다."
    }
  },
  {
    "id": "advice_33",
    "document": "비를 원한다면, 진흙도 피할 수 없다는 걸 받아들여야 해.",
    "metadata": {
      "author": "덴젤 워싱턴",
      "authorProfile": "영화 배우",
      "message": "비가 내리기 바란다면 진흙과도 상대해야한다. 피할 수 없는 것이다."
    }
  },
  {
    "id": "advice_34",
    "document": "자신감 있는 표정을 짓다 보면 진짜 자신감도 생겨요.",
    "metadata": {
      "author": "찰스 다윈",
      "authorProfile": "생물 학자, <종의 기원>의 저자",
      "message": "자신감 있는 표정을 지으면 자신감이 생긴다."
    }
  },
  {
    "id": "advice_35",
    "document": "의심을 받을 때도 자신을 믿고 지지하는 자신만의 응원자가 되어 주세요.",
    "metadata": {
      "author": "너새니얼 호손",
      "authorProfile": "작가, <주홍글씨>의 저자",
      "message": "회의적인 세상이 지독한 의심으로 자신을 공격해도 언제나 자신을 믿어야 한다. 전 인류에 맞서 자신의 유일한 사도가 되어야 한다."
    }
  },
  {
    "id": "advice_36",
    "document": "인생은 탄생(B)과 죽음(D) 사이에서 선택(C)하는 과정이에요.",
    "metadata": {
      "author": "장 폴 사르트르",
      "authorProfile": "작가, 철학자",
      "message": "인생은 B(brith)와 D(death)사이의 C(choice)다."
    }
  },
  {
    "id": "advice_37",
    "document": "행복해지려면 다른 사람들을 너무 신경 쓰지 마세요.",
    "metadata": {
      "author": "알베르 카뮈",
      "authorProfile": "작가, 철학자",
      "message": "행복하기 위해선 절대 다른 사람들을 너무 의식해서는 안 된다."
    }
  },
  {
    "id": "advice_38",
    "document": "우리는 아침에 일어나기를 기대할 이유가 필요해요. 여러분에게는 어떤 이유가 있나요?",
    "metadata": {
      "author": "일론 머스크",
      "authorProfile": "스페이스X 창업자, 테슬라 CEO",
      "message": "우리가 아침에 일어나서 살아가고 싶게 만드는 이유가 있어야 한다. 여러분은 왜 살려고 하는가?"
    }
  },
  {
    "id": "advice_39",
    "document": "열정 없는 삶은 의미가 없으니, 뜨거운 열정을 가지고 살아가야 해요.",
    "metadata": {
      "author": "커트 코베인",
      "authorProfile": "너바나 보컬, 기타리스트",
      "message": "열정없이 사느니 차라리 죽는게 낫다."
    }
  },
  {
    "id": "advice_40",
    "document": "외부에서 힘과 자신감을 찾으려 해도, 사실 그것들은 언제나 내 안에 있다는 걸 잊지 마세요.",
    "metadata": {
      "author": "안나 프로이트",
      "authorProfile": "정신분석학자",
      "message": "힘과 자신감을 외부에서 찾으려 노력했지만, 이는 전부 내면에서 나온다. 늘 이곳에 있다."
    }
  },
  {
    "id": "advice_41",
    "document": "위대한 사람은 목표를 갖고, 보통 사람은 바람만 갖고 있다.",
    "metadata": {
      "author": "워싱턴 어빙",
      "authorProfile": "작가",
      "message": "위대한 인물에게는 목표가 있고 평범한 사람들에게는 소망이 있을 뿐이다."
    }
  },
  {
    "id": "advice_42",
    "document": "인생에서 가장 좋은 것들은 종종 두려움의 벽 너머에 있어요. 용기를 내어 그 벽을 넘어서야 해요.",
    "metadata": {
      "author": "윌 스미스",
      "authorProfile": "영화 배우",
      "message": "신은 인생에서 최고의 것들을 항상 두려움 뒤에 놓습니다."
    }
  },
  {
    "id": "advice_43",
    "document": "모든 성취는 작은 열망에서 시작됩니다.",
    "metadata": {
      "author": "나폴레온 힐",
      "authorProfile": "작가, 세계적인 성공학 연구자",
      "message": "모든 성취의 시작점은 갈망이다."
    }
  },
  {
    "id": "advice_44",
    "document": "배운 것이 없다고 생각하기에, 어떤 것이든 편견 없이 배우고 받아들일 수 있다는 의미예요.",
    "metadata": {
      "author": "마쓰씨타 고노스케",
      "authorProfile": "마쓰시타사 창업자",
      "message": "나는 배운게 없기 때문에 모르는게 없다."
    }
  },
  {
    "id": "advice_45",
    "document": "실수하면서 살아온 삶은 아무것도 하지 않은 삶보다 훨씬 가치 있고 존경할 만하답니다.",
    "metadata": {
      "author": "조지 버나드 쇼",
      "authorProfile": "극작가, 사회주의자",
      "message": "실수하며 보낸 인생은 아무것도 하지 않은 인생보다 존경스러울 뿐 아니라 더 유용하다."
    }
  },
  {
    "id": "advice_46",
    "document": "가장 큰 영광은 실패하지 않는 것이 아니라, 실패해도 다시 힘차게 일어서는 데 있습니다.",
    "metadata": {
      "author": "공자",
      "authorProfile": "유학자, 세계 4대 성인",
      "message": "가장 큰 영광은 한 번도 실패하지 않음이 아니라, 실패할 때마다 다시 일어서는데 있다."
    }
  },
  {
    "id": "advice_47",
    "document": "난 더 열심히 노력할수록 행운이 더 많이 찾아온다는 걸 알게 됐어.",
    "metadata": {
      "author": "토마스 제퍼슨",
      "authorProfile": "미국 3대 대통령",
      "message": "나는 내가 더 노력할 수록 운이 더 좋아진다는 것을 발견했다."
    }
  },
  {
    "id": "advice_48",
    "document": "희망이 있는 곳에는 항상 도전이 함께합니다.",
    "metadata": {
      "author": "무라카미 하루키",
      "authorProfile": "작가",
      "message": "희망이 있는 곳에 반드시 시련이 있는 법이다."
    }
  },
  {
    "id": "advice_49",
    "document": "힘든 시기를 겪고 있다면, 멈추지 말고 계속 나아가세요. 그 끝은 분명히 있습니다.",
    "metadata": {
      "author": "윈스턴 처칠",
      "authorProfile": "영국 총리",
      "message": "지옥을 겪고 있다면 계속 겪어 나가라."
    }
  },
  {
    "id": "advice_50",
    "document": "미래의 어려움을 대비하지 않는다면, 언젠가 지난날의 나태함을 후회하게 될 거예요.",
    "metadata": {
      "author": "헨리 클레이",
      "authorProfile": "정치인, 위대한 중재자",
      "message": "겨울이 당신에게 여름 내내 무얼 했느냐 묻는 날이 꼭 올 것이다."
    }
  },
  {
    "id": "advice_51",
    "document": "미래를 만드는 것이야말로 그 미래를 예측하는 가장 좋은 방법입니다.",
    "metadata": {
      "author": "앨런 케이",
      "authorProfile": "컴퓨터과학자, OOP의 선구자",
      "message": "미래를 예측하는 최선의 방법은 미래를 창조하는 것이다."
    }
  },
  {
    "id": "advice_52",
    "document": "나는 폭풍을 두려워하지 않아. 배를 타고 항해하는 법을 배우고 있거든.",
    "metadata": {
      "author": "헬렌 켈러",
      "authorProfile": "인문계 학사를 받은 최초의 시청각 장애인",
      "message": "나는 폭풍이 두렵지 않다. 나는 배로 항해 하는 법을 배우고 있으니까."
    }
  },
  {
    "id": "advice_53",
    "document": "우리의 모든 꿈은 이루어질 수 있어요. 그 꿈을 좇을 용기만 있다면 말이죠.",
    "metadata": {
      "author": "월트 디즈니",
      "authorProfile": "월트 디즈니 컴퍼니 창업자",
      "message": "우리의 모든 꿈은 이루어질 것이다. 그들을 믿고 나갈 용기만 있다면"
    }
  },
  {
    "id": "advice_54",
    "document": "결심한 일은 꼭 해내세요. 용감하게 도전하세요.",
    "metadata": {
      "author": "벤자민 프랭클린",
      "authorProfile": "정치인, 미국 건국의 아버지",
      "message": "해야할 일은 과감히 하라. 결심한 일은 반드시 실행하라."
    }
  },
  {
    "id": "advice_55",
    "document": "꿈을 날짜와 함께 기록하면 목표가 되고, 이를 작게 나누면 계획이 되어, 계획을 실행하면 꿈은 이루어집니다.",
    "metadata": {
      "author": "그렉 S 리드",
      "authorProfile": "작가",
      "message": "꿈을 날짜와 함께 적어 놓으면 목표가 되고, 목표를 잘게 나누면 계획이 되며, 계획을 실행에 옮기면 꿈은 실현되는 것이다."
    }
  },
  {
    "id": "advice_56",
    "document": "절대 포기하지 마세요.",
    "metadata": {
      "author": "윈스턴 처칠",
      "authorProfile": "영국 총리",
      "message": "절대로, 절대로, 절대로, 절대로 포기하지 마라."
    }
  },
  {
    "id": "advice_57",
    "document": "강해서 이기는 게 아니라, 이기는 사람이 결국 강한 사람이라는 뜻이에요.",
    "metadata": {
      "author": "프란츠 베켄바우어",
      "authorProfile": "축구 선수, 리베로의 창시자",
      "message": "강한 자가 이기는 것이 아니라, 이긴 자가 강한 것이다."
    }
  },
  {
    "id": "advice_58",
    "document": "지금 시작하는 것이 가장 좋은 때야. 너무 늦었다고 생각하지 마.",
    "metadata": {
      "author": "박명수",
      "authorProfile": "코미디언",
      "message": "늦었다고 생각할 때가 진짜 너무 늦었다. 그러니 지금 당장 시작해라."
    }
  },
  {
    "id": "advice_59",
    "document": "모든 약점은 강점으로 바뀔 수 있어.",
    "metadata": {
      "author": "리오넬 메시",
      "authorProfile": "축구 선수, 발롱도르 최다 수상자",
      "message": "모든 단점은, 장점이 될 수 있다."
    }
  },
  {
    "id": "advice_60",
    "document": "제 목표는 항상 최선을 다해 최고가 되는 것입니다. 2등이 아닌 1등을 목표로 하세요.",
    "metadata": {
      "author": "문호준",
      "authorProfile": "카트라이더 프로게이머",
      "message": "목표는 당연히 우승이죠. 저는 준우승을 모릅니다."
    }
  },
  {
    "id": "advice_61",
    "document": "배는 항구에 머무르면 안전하지만, 본래 바다로 나아가야 그 의미를 찾을 수 있어요.",
    "metadata": {
      "author": "존 A. 쉐드",
      "authorProfile": "교육자",
      "message": "항구에 정박해 있는 배는 안전하다. 그러나 그것이 배의 존재 이유는 아니다."
    }
  },
  {
    "id": "advice_62",
    "document": "해보지 않았다면 확신하기 어려울 수 있어요.",
    "metadata": {
      "author": "김병만",
      "authorProfile": "달인",
      "message": "안 해 봤으면 말을 하지 마세요."
    }
  },
  {
    "id": "advice_63",
    "document": "여러가지 방식으로 함께 갈 수 있지만, 최종적으로는 자신의 한 걸음이 필요하다.",
    "metadata": {
      "author": "헤르만 헤세",
      "authorProfile": "작가, <데미안>의 저자",
      "message": "말로 갈 수도, 차로 갈 수도, 둘이서 갈 수도, 셋이서 갈 수도 있다. 하지만 맨 마지막 한 걸음은 자기 혼자서 걷지 않으면 안된다."
    }
  },
  {
    "id": "advice_64",
    "document": "많은 사람들이 세상을 변화시키려 하지만, 자신부터 변화하려는 사람은 드물다.",
    "metadata": {
      "author": "레프 톨스토이",
      "authorProfile": "작가, 러시아의 대문호",
      "message": "모두가 세상을 변화시키려 하지만, 정작 스스로 변하겠다고 생각하는 사람은 없다."
    }
  },
  {
    "id": "advice_65",
    "document": "용기는 두려움을 느끼지 않는 것이 아니라, 두려워도 잠시 더 참아내는 거예요.",
    "metadata": {
      "author": "조지 패튼",
      "authorProfile": "미국의 장군",
      "message": "용기란 공포를 1분 더 참는 것이다."
    }
  },
  {
    "id": "advice_66",
    "document": "어떤 일이 불가능하다고 믿으면, 그 일이 진짜 불가능해질 수 있어요. ‍🌈💪✨",
    "metadata": {
      "author": "풀러",
      "authorProfile": "학자",
      "message": "일이 불가능하다고 믿는 것은 일을 불가능하게 하는 일이다."
    }
  },
  {
    "id": "advice_67",
    "document": "아이디어의 가치는 실행에 달려있어요.",
    "metadata": {
      "author": "카를로스 곤",
      "authorProfile": "브라질의 기업인",
      "message": "아이디어의 좋고 나쁨은 어떻게 실행하느냐에 따라 결정된다."
    }
  },
  {
    "id": "advice_68",
    "document": "잠잘 때도 수입이 생기는 방법을 찾지 않으면 계속 일해야 할 거예요.",
    "metadata": {
      "author": "워렌 버핏",
      "authorProfile": "버크셔 해서웨이 CEO, 오마하의 현인",
      "message": "잠자는 동안에도 돈이 들어오는 방법을 찾지 못한다면, 당신은 죽을 때까지 일을 해야만 할 것이다."
    }
  },
  {
    "id": "advice_69",
    "document": "어려움을 이겨내면 더 강해질 수 있어요.",
    "metadata": {
      "author": "프리드리히 니체",
      "authorProfile": "철학자",
      "message": "나를 죽이지 못하는 것은 나를 강하게 만든다."
    }
  },
  {
    "id": "advice_70",
    "document": "실패는 가능성이 있는 일입니다. 실패를 통해 우리는 더 혁신적으로 발전할 수 있습니다.",
    "metadata": {
      "author": "일론 머스크",
      "authorProfile": "스페이스X 창업자, 테슬라 CEO",
      "message": "실패는 옵션이다. 실패하지 않는다면, 당신은 충분한 혁신을 이룰 수 없다."
    }
  },
  {
    "id": "advice_71",
    "document": "실패는 두려워하지 마세요. 한 번만 성공하면 됩니다.",
    "metadata": {
      "author": "드류 휴스턴",
      "authorProfile": "드롭박스 공동 창업자",
      "message": "실패에 대해 걱정하지 마라. 한번만 제대로 하면 된다."
    }
  },
  {
    "id": "advice_72",
    "document": "혁신을 하면 사람들이 미쳤다고 할 수 있으니, 그런 말에 대비하세요.",
    "metadata": {
      "author": "래리 앨리슨",
      "authorProfile": "오라클 CEO",
      "message": "혁신을 할 때는 모든 사람들이 당신을 미쳤다고 할 테니, 그들 말에 준비가 되어 있어야 한다."
    }
  },
  {
    "id": "advice_73",
    "document": "가난하게 태어난 것은 내 책임이 아닙니다. 그러나 가난하게 죽는다면, 그것은 내 선택이며 내 책임입니다.",
    "metadata": {
      "author": "빌 게이츠",
      "authorProfile": "마이크로소프트 창업자",
      "message": "내가 가난하게 태어났다면, 결코 내 탓이 아니다. 하지만 만약 내가 가난하게 세상을 떠난다면, 모두 내 잘못이다."
    }
  },
  {
    "id": "advice_74",
    "document": "'지금이 최악'이라고 말할 수 있다면, 상황이 최악은 아니니 희망을 가질 수 있어요.",
    "metadata": {
      "author": "셰익스피어",
      "authorProfile": "극작가, 역사상 가장 위대한 작가",
      "message": "'지금이 최악'이라고 말할 힘이 있다면 아직 최악은 아니다."
    }
  },
  {
    "id": "advice_75",
    "document": "장애가 있을 때 포기할지, 그것을 극복하려 노력할지는 당신의 선택입니다.",
    "metadata": {
      "author": "김수영",
      "authorProfile": "작가",
      "message": "당신을 가로막는 장애때문에 포기할 것인가, 반대로 그 장애를 넘어서기 위해 노력할 것인가는 당신이 선택할 문제다."
    }
  },
  {
    "id": "advice_76",
    "document": "배운 것을 실제로 사용하고 실행으로 옮기는 게 중요해요.",
    "metadata": {
      "author": "괴테",
      "authorProfile": "작가, 독일의 가장 위대한 문인",
      "message": "아는 것만으로는 충분하지 않다. 적용해야만 한다. 의지만으로 충분하지 않다. 실행해야 한다."
    }
  },
  {
    "id": "advice_77",
    "document": "당신이 2위로 만족한다고 말하면, 결국 그렇게 될 가능성이 크다는 것을 알게 되었어요.",
    "metadata": {
      "author": "존 F. 케네디",
      "authorProfile": "미국 35대 대통령",
      "message": "당신이 자신은 2위로 만족한다고 일단 말하면, 당신의 인생은 그렇게 되기 마련이라는 것을 나는 깨달았다."
    }
  },
  {
    "id": "advice_78",
    "document": "성공하려면 잘하는 일에 열정을 가지고 집중하는 것이 중요해요.",
    "metadata": {
      "author": "톰 매너한",
      "authorProfile": "도미노피자 창업자",
      "message": "성공의 비결은 단 한 가지, 잘할 수 있는 일에 광적으로 집중하는 것이다."
    }
  },
  {
    "id": "advice_79",
    "document": "시련이 있더라도 포기하지 않으면 실패는 없어요.",
    "metadata": {
      "author": "정주영",
      "authorProfile": "현대그룹의 창업자",
      "message": "시련은 있어도 실패는 없다."
    }
  },
  {
    "id": "advice_80",
    "document": "무언가를 시도해보기도 전에 지레 겁먹고 포기하지는 않았나요? 일단 도전해보는 정신이 중요해요.",
    "metadata": {
      "author": "정주영",
      "authorProfile": "현대그룹의 창업자",
      "message": "이봐 해봤어?"
    }
  },
  {
    "id": "advice_81",
    "document": "열정을 그저 생존이 아닌 변화를 위해 사용해보세요.",
    "metadata": {
      "author": "덴젤 워싱턴",
      "authorProfile": "영화 배우",
      "message": "살기 위해 열정을 쏟지 마라. 다름을 만들기 위해 열정을 사용해라."
    }
  },
  {
    "id": "advice_82",
    "document": "실패가 없다면 시도도 없다는 뜻이야. 실패는 배움의 과정 중 하나니까 두려워 말고 도전해보자!",
    "metadata": {
      "author": "덴젤 워싱턴",
      "authorProfile": "영화 배우",
      "message": "실패를 하지 않는다면 너는 시도조차 하지 않는 것이다."
    }
  },
  {
    "id": "advice_83",
    "document": "진정한 성공은 꾸준한 노력을 통해 이뤄집니다.",
    "metadata": {
      "author": "마이클 조던",
      "authorProfile": "농구 황제",
      "message": "진정한 성공에 지름길은 없다."
    }
  },
  {
    "id": "advice_84",
    "document": "중요한 일이라면 어려움이 있어도 포기하지 말고 계속하세요.",
    "metadata": {
      "author": "일론 머스크",
      "authorProfile": "스페이스X 창업자, 테슬라 CEO",
      "message": "정말 중요한 일이라면 역경이 닥쳐도 그 일을 계속해야 합니다."
    }
  },
  {
    "id": "advice_85",
    "document": "성공에 한 걸음 더 다가가려면 여러분이 할 수 있는 만큼 최선을 다하고 많은 시간을 투자하는 것이 중요합니다.",
    "metadata": {
      "author": "일론 머스크",
      "authorProfile": "스페이스X 창업자, 테슬라 CEO",
      "message": "당신이 할 수 있는 만큼 정말로 열심히 일하세요. 적어도 일주일에 80-100시간 가량 투자해야 합니다. 그게 성공에 가까이 가는 지름길입니다."
    }
  },
  {
    "id": "advice_86",
    "document": "생각의 경계를 넘어서 최선을 다할 때 진정한 '혼신'이 나타나요.",
    "metadata": {
      "author": "유재석",
      "authorProfile": "코미디언, 국민 MC",
      "message": "내가 생각하는 범위에서 최선을 다하면 안돼. 그걸 벗어나서 최선을 다해야지 그게 '혼신'이야."
    }
  },
  {
    "id": "advice_87",
    "document": "잘 해내자! 하나씩, 차근차근, 눈앞의 목표부터 집중하세요.",
    "metadata": {
      "author": "김연아",
      "authorProfile": "피겨여왕, 21세기 여자 피겨 최고의 선수",
      "message": "이걸 잘하자! 이걸 하고 나면 그 다음.. 그리고 그 다음.. 그렇게 눈앞에 보이는 지점에 집중했어요."
    }
  },
  {
    "id": "advice_88",
    "document": "다른 사람들이 쉽게 할 수 있는 일보다, 당신만이 특별하게 할 수 있는 일을 찾아보세요.",
    "metadata": {
      "author": "아멜리아 에어하트",
      "authorProfile": "파일럿, 여성 최초 대서양 횡비행",
      "message": "다른 사람들이 할 수 있거나 할 일을 하지 말고, 다른 이들이 할 수 없고 하지 않을 일들을 하라."
    }
  },
  {
    "id": "advice_89",
    "document": "나중에 후회하지 않도록, 해야겠다고 마음먹었을 때 바로 실천에 옮기는 것이 중요해요.",
    "metadata": {
      "author": "익명",
      "authorProfile": "-",
      "message": "라고 할때 할걸"
    }
  },
  {
    "id": "advice_90",
    "document": "시작할 때는 그 결과를 알 수 없지만, 과정을 통해 명확해집니다. 중요한 것은 일단 시작하는 것입니다.",
    "metadata": {
      "author": "마크 주커버그",
      "authorProfile": "페이스북의 창업자",
      "message": "시작할 때는 아무도 모릅니다. 실행하는 과정을 통해 명확해집니다. 일단 시작하는 게 중요합니다."
    }
  },
  {
    "id": "advice_91",
    "document": "정말 중요하지 않아서 죽기 전에 마무리하지 않아도 될 일만 내일로 미루세요.",
    "metadata": {
      "author": "파블로 피카소",
      "authorProfile": "작가",
      "message": "마치지 않고 죽어도 되는 일만 내일로 미뤄라."
    }
  },
  {
    "id": "advice_92",
    "document": "동기 부여는 오래 가지 않을 수 있어요. 그래서 매일 꾸준히 해야 해요, 마치 매일 샤워를 하는 것처럼요.",
    "metadata": {
      "author": "지그 지글러",
      "authorProfile": "동기부여 연설가",
      "message": "사람들이 동기 부여는 오래가지 않는다고 말한다. 목욕도 마찬가지다. 그래서 매일 하라고 하는 것이다."
    }
  },
  {
    "id": "advice_93",
    "document": "'당신이 얼마나 바쁜지가 아니라, 무엇에 바쁜지가 더 중요해요.'",
    "metadata": {
      "author": "오프라 윈프리",
      "authorProfile": "방송인, 흑인 여성 중 가장 성공한 인물 중 한명",
      "message": "중요한 질문은 '당신이 얼마나 바쁜가?'가 아니다. '당신이 무엇에 바쁜가'가 핵심 질문이다."
    }
  },
  {
    "id": "advice_94",
    "document": "누군가의 진정한 모습을 알고 싶다면, 그 사람에게 권력을 줘보세요.",
    "metadata": {
      "author": "에이브러햄 링컨",
      "authorProfile": "미국 16대 대통령",
      "message": "만약 당신이 누군가의 인격을 시험해 보고 싶다면, 그에게 권력을 줘 보라."
    }
  },
  {
    "id": "advice_95",
    "document": "때로는 말을 아끼고 침묵을 지키는 것이 좋습니다.",
    "metadata": {
      "author": "루드비히 비트겐슈타인",
      "authorProfile": "철학자",
      "message": "말할 수 없는 것에 대해서는 침묵해야 한다."
    }
  },
  {
    "id": "advice_96",
    "document": "가끔 말이 안 떠오를 때, 우리는 감정적으로 반응할 수 있어요.",
    "metadata": {
      "author": "볼테르",
      "authorProfile": "작가",
      "message": "사람들은 할 말이 없으면 욕을 한다."
    }
  },
  {
    "id": "advice_97",
    "document": "더 깊고 복잡한 세계는 단순한 관점으로는 온전히 이해하기 어려울 수 있다는 의미입니다.",
    "metadata": {
      "author": "프리드리히 니체",
      "authorProfile": "철학자",
      "message": "한낱 빛 따위가 어찌 어둠을 알 랴."
    }
  },
  {
    "id": "advice_98",
    "document": "창조란 서로 다른 것들을 이어주는 힘입니다.",
    "metadata": {
      "author": "스티브 잡스",
      "authorProfile": "애플의 창업자",
      "message": "창조란 모든 것을 연결하는 것이다."
    }
  },
  {
    "id": "advice_99",
    "document": "누군가를 믿기로 했다면 마음을 열고 신뢰하십시오.",
    "metadata": {
      "author": "구인회",
      "authorProfile": "LG그룹의 창업자",
      "message": "한 번 사람을 믿으면 모두 맡기십시오."
    }
  },
  {
    "id": "advice_100",
    "document": "좋은 예술가는 다른 작품에서 영감을 얻고, 훌륭한 예술가는 그 영감을 자신만의 독창적인 것으로 만들어냅니다.",
    "metadata": {
      "author": "파블로 피카소",
      "authorProfile": "화가",
      "message": "좋은 예술가는 베끼고, 훌륭한 예술가는 훔친다."
    }
  },
  {
    "id": "advice_101",
    "document": "SNS에 너무 많은 시간을 쏟기보다는, 삶 속에서 더 많은 가치를 찾아보는 것도 좋을 것 같아요.",
    "metadata": {
      "author": "알렉스 퍼거슨",
      "authorProfile": "축구 감독",
      "message": "트위터는 인생의 낭비다. 인생에선 더 많은 것들을 할 수 있다."
    }
  },
  {
    "id": "advice_102",
    "document": "주식 투자는 언제나 위험하지만, 10월은 특히 주의해야 할 달입니다. 사실, 모든 달이 조심할 만한 이유를 가지고 있죠.",
    "metadata": {
      "author": "마크 트웨인",
      "authorProfile": "작가",
      "message": "10월, 주식 투자에 특히 위험한 달 중 하나다. 다른 위험한 달로는 7월, 1월, 9월, 4월, 11월, 5월, 3월, 6월, 12월, 8월, 그리고 2월이 있다."
    }
  },
  {
    "id": "advice_103",
    "document": "큰 하락이나 어려움을 겪은 후에는 종종 큰 성장이나 기회가 찾아온다는 의미입니다.",
    "metadata": {
      "author": "증권 시장의 격언",
      "authorProfile": "-",
      "message": "골이 깊으면 산도 높다."
    }
  }
]


SAMPLE_PAST_DIARY_DATA = [
  {
    "id": "user001_20250728115553_1",
    "document": "팀장님이 내 아이디어를 채택해주셔서 정말 뿌듯했다. 오랫동안 고민했던 제안이 인정받는 느낌이었다.",
    "metadata": {
      "user_id": "user001",
      "date": "2025.07.28",
      "emotion": "긍정적 감정",
      "situation": "업무 및 학습"
    }
  },
  {
    "id": "user002_20250728115553_2",
    "document": "새로운 취미로 시작한 그림 그리기가 생각보다 어려워서 좌절감이 든다. 계속 해볼 수 있을까 싶다.",
    "metadata": {
      "user_id": "user002",
      "date": "2025.07.28",
      "emotion": "수치와 자책",
      "situation": "창작과 성장"
    }
  },
  {
    "id": "user003_20250728115553_3",
    "document": "친구와 카페에서 오랜만에 수다를 떨었는데, 시간 가는 줄 몰랐다. 역시 좋은 사람과 함께하는 시간은 소중하다.",
    "metadata": {
      "user_id": "user003",
      "date": "2025.07.27",
      "emotion": "긍정적 감정",
      "situation": "일상 및 여가"
    }
  },
  {
    "id": "user004_20250728115553_4",
    "document": "갑작스런 발표 요청에 심장이 두근거리고 손에 땀이 났다. 사람들 앞에서 말하는 게 아직도 무섭다.",
    "metadata": {
      "user_id": "user004",
      "date": "2025.07.26",
      "emotion": "두려움과 공포",
      "situation": "업무 및 학습"
    }
  },
  {
    "id": "user005_20250728115553_5",
    "document": "건강검진 결과를 기다리는 동안 계속 불안했다. 작은 증상도 큰 병일까 봐 걱정된다.",
    "metadata": {
      "user_id": "user005",
      "date": "2025.07.25",
      "emotion": "불안과 긴장",
      "situation": "건강 및 의료"
    }
  },
  {
    "id": "user006_20250728115553_6",
    "document": "온라인에서 나에 대한 부정적인 댓글을 봤는데, 하루 종일 기분이 상했다. 인터넷은 정말 무서운 곳이다.",
    "metadata": {
      "user_id": "user006",
      "date": "2025.07.24",
      "emotion": "소외와 상실",
      "situation": "디지털 및 온라인 활동"
    }
  },
  {
    "id": "user007_20250728115553_7",
    "document": "어릴 적 살던 동네를 지나가다가 문득 그때가 그리워졌다. 무엇 하나 걱정 없던 그 시절로 돌아가고 싶다.",
    "metadata": {
      "user_id": "user007",
      "date": "2025.07.23",
      "emotion": "그리움과 아쉬움",
      "situation": "내면 활동 및 감정"
    }
  },
  {
    "id": "user008_20250728115553_8",
    "document": "새로운 프로젝트에 참여하게 되어 의욕이 넘친다. 이번에는 정말 좋은 결과를 만들어보고 싶다.",
    "metadata": {
      "user_id": "user008",
      "date": "2025.07.22",
      "emotion": "동기와 욕구",
      "situation": "업무 및 학습"
    }
  },
  {
    "id": "user009_20250728115553_9",
    "document": "생일 파티에서 친구들이 깜짝 선물을 준비해줘서 너무 감동받았다. 이런 친구들이 있어서 행복하다.",
    "metadata": {
      "user_id": "user009",
      "date": "2025.07.21",
      "emotion": "긍정적 감정",
      "situation": "특별한 날과 사건"
    }
  },
  {
    "id": "user010_20250728115553_10",
    "document": "동료와의 갈등으로 인해 팀 분위기가 어색해졌다. 어떻게 해결해야 할지 모르겠어서 답답하다.",
    "metadata": {
      "user_id": "user010",
      "date": "2025.07.20",
      "emotion": "사회적 관계 감정",
      "situation": "인간관계"
    }
  },
  {
    "id": "user011_20250728115553_11",
    "document": "주말 내내 집에서 넷플릭스만 봤는데, 뭔가 시간을 허비한 것 같아 허무하다.",
    "metadata": {
      "user_id": "user011",
      "date": "2025.07.19",
      "emotion": "이완과 침체",
      "situation": "일상 및 여가"
    }
  },
  {
    "id": "user012_20250728115553_12",
    "document": "새로운 기술을 배우려고 하는데 너무 복잡해서 혼란스럽다. 내가 따라갈 수 있을까 의심된다.",
    "metadata": {
      "user_id": "user012",
      "date": "2025.07.18",
      "emotion": "혼란과 의심",
      "situation": "업무 및 학습"
    }
  },
  {
    "id": "user013_20250728115553_13",
    "document": "콘서트에서 좋아하는 가수를 직접 보니까 정말 감동적이었다. 이런 순간이 있어서 삶이 아름답다고 느꼈다.",
    "metadata": {
      "user_id": "user013",
      "date": "2025.07.17",
      "emotion": "경이와 압도",
      "situation": "특별한 날과 사건"
    }
  },
  {
    "id": "user014_20250728115553_14",
    "document": "급여가 인상되어서 기분이 좋다. 그동안의 노력이 인정받은 것 같아 뿌듯하다.",
    "metadata": {
      "user_id": "user014",
      "date": "2025.07.16",
      "emotion": "긍정적 감정",
      "situation": "경제 및 소비생활"
    }
  },
  {
    "id": "user015_20250728115553_15",
    "document": "병원에서 검사받는 동안 계속 떨렸다. 의사선생님이 무서운 말을 하면 어떡하지 싶었다.",
    "metadata": {
      "user_id": "user015",
      "date": "2025.07.15",
      "emotion": "두려움과 공포",
      "situation": "건강 및 의료"
    }
  },
  {
    "id": "user016_20250728115553_16",
    "document": "온라인 쇼핑에서 실수로 잘못 주문했는데, 환불 과정이 복잡해서 스트레스받는다.",
    "metadata": {
      "user_id": "user016",
      "date": "2025.07.14",
      "emotion": "불안과 긴장",
      "situation": "디지털 및 온라인 활동"
    }
  },
  {
    "id": "user017_20250728115553_17",
    "document": "실수로 동료에게 상처되는 말을 했다. 나는 왜 항상 이런 실수를 반복할까 자책하게 된다.",
    "metadata": {
      "user_id": "user017",
      "date": "2025.07.13",
      "emotion": "수치와 자책",
      "situation": "인간관계"
    }
  },
  {
    "id": "user018_20250728115553_18",
    "document": "오랫동안 연락하지 못한 친구가 떠올라서 그립다. 예전처럼 자주 만날 수 있었으면 좋겠다.",
    "metadata": {
      "user_id": "user018",
      "date": "2025.07.12",
      "emotion": "그리움과 아쉬움",
      "situation": "인간관계"
    }
  },
  {
    "id": "user019_20250728115553_19",
    "document": "새로운 언어를 배우고 싶은 욕구가 생겼다. 외국 여행을 가서 현지인과 대화해보고 싶다.",
    "metadata": {
      "user_id": "user019",
      "date": "2025.07.11",
      "emotion": "동기와 욕구",
      "situation": "창작과 성장"
    }
  },
  {
    "id": "user020_20250728115553_20",
    "document": "가족 모임에서 모든 친척들이 화목하게 지내는 모습을 보니 마음이 따뜻해졌다.",
    "metadata": {
      "user_id": "user020",
      "date": "2025.07.10",
      "emotion": "사회적 관계 감정",
      "situation": "특별한 날과 사건"
    }
  },
  {
    "id": "user021_20250728115553_21",
    "document": "비 오는 날 집에서 책을 읽으며 차를 마시니까 정말 평온하다. 이런 여유로운 시간이 좋다.",
    "metadata": {
      "user_id": "user021",
      "date": "2025.07.09",
      "emotion": "이완과 침체",
      "situation": "일상 및 여가"
    }
  },
  {
    "id": "user022_20250728115553_22",
    "document": "진로에 대해 고민이 많아진다. 내가 정말 원하는 것이 무엇인지 확신이 서지 않는다.",
    "metadata": {
      "user_id": "user022",
      "date": "2025.07.08",
      "emotion": "혼란과 의심",
      "situation": "내면 활동 및 감정"
    }
  },
  {
    "id": "user023_20250728115553_23",
    "document": "산 정상에서 바라본 일출이 너무 아름다워서 말문이 막혔다. 자연의 위대함 앞에서 겸손해진다.",
    "metadata": {
      "user_id": "user023",
      "date": "2025.07.07",
      "emotion": "경이와 압도",
      "situation": "일상 및 여가"
    }
  },
  {
    "id": "user024_20250728115553_24",
    "document": "로또에 당첨되지 않아서 아쉽지만, 그래도 꿈을 꾸는 재미가 있었다.",
    "metadata": {
      "user_id": "user024",
      "date": "2025.07.06",
      "emotion": "그리움과 아쉬움",
      "situation": "경제 및 소비생활"
    }
  },
  {
    "id": "user025_20250728115553_25",
    "document": "요리를 배우고 싶어서 유튜브 영상을 보며 연습하고 있다. 맛있는 음식을 만들고 싶다는 의욕이 크다.",
    "metadata": {
      "user_id": "user025",
      "date": "2025.07.05",
      "emotion": "동기와 욕구",
      "situation": "일상 및 여가"
    }
  },
  {
    "id": "user026_20250728115553_26",
    "document": "회사에서 승진 발표가 있었는데 내 이름이 없어서 실망스럽다. 더 열심히 해야겠다는 생각이 든다.",
    "metadata": {
      "user_id": "user026",
      "date": "2025.07.04",
      "emotion": "소외와 상실",
      "situation": "업무 및 학습"
    }
  },
  {
    "id": "user027_20250728115553_27",
    "document": "SNS에서 다른 사람들의 행복한 모습을 보니까 나만 뒤처진 것 같아서 우울해진다.",
    "metadata": {
      "user_id": "user027",
      "date": "2025.07.03",
      "emotion": "수치와 자책",
      "situation": "디지털 및 온라인 활동"
    }
  },
  {
    "id": "user028_20250728115553_28",
    "document": "오랜만에 부모님과 함께 식사하며 대화를 나누니까 마음이 편안해졌다.",
    "metadata": {
      "user_id": "user028",
      "date": "2025.07.02",
      "emotion": "긍정적 감정",
      "situation": "인간관계"
    }
  },
  {
    "id": "user029_20250728115553_29",
    "document": "갑작스런 응급실 방문으로 가족들이 모두 걱정했다. 건강의 소중함을 다시 한번 깨달았다.",
    "metadata": {
      "user_id": "user029",
      "date": "2025.07.01",
      "emotion": "두려움과 공포",
      "situation": "건강 및 의료"
    }
  },
  {
    "id": "user030_20250728115553_30",
    "document": "중요한 프레젠테이션을 앞두고 있어서 계속 긴장된다. 실수하지 않으려면 어떻게 해야 할까.",
    "metadata": {
      "user_id": "user030",
      "date": "2025.06.30",
      "emotion": "불안과 긴장",
      "situation": "업무 및 학습"
    }
  },
  {
    "id": "user031_20250728115553_31",
    "document": "새로운 취미 활동으로 등산을 시작했는데, 체력이 부족해서 많이 힘들었다. 꾸준히 해야겠다.",
    "metadata": {
      "user_id": "user031",
      "date": "2025.06.29",
      "emotion": "수치와 자책",
      "situation": "일상 및 여가"
    }
  },
  {
    "id": "user032_20250728115553_32",
    "document": "졸업식에서 친구들과 마지막 인사를 나누며 아쉬움이 많이 남았다. 앞으로도 연락하며 지내자고 약속했다.",
    "metadata": {
      "user_id": "user032",
      "date": "2025.06.28",
      "emotion": "그리움과 아쉬움",
      "situation": "특별한 날과 사건"
    }
  },
  {
    "id": "user033_20250728115553_33",
    "document": "새로운 직장에서 일하고 싶다는 욕구가 강해졌다. 더 나은 환경에서 성장하고 싶다.",
    "metadata": {
      "user_id": "user033",
      "date": "2025.06.27",
      "emotion": "동기와 욕구",
      "situation": "업무 및 학습"
    }
  },
  {
    "id": "user034_20250728115553_34",
    "document": "팀 프로젝트에서 모든 구성원들이 협력하는 모습이 보기 좋았다. 이런 팀워크가 있으면 뭐든 할 수 있을 것 같다.",
    "metadata": {
      "user_id": "user034",
      "date": "2025.06.26",
      "emotion": "사회적 관계 감정",
      "situation": "업무 및 학습"
    }
  },
  {
    "id": "user035_20250728115553_35",
    "document": "스파에서 마사지를 받으며 완전히 릴렉스했다. 오랜만에 몸과 마음이 편안해졌다.",
    "metadata": {
      "user_id": "user035",
      "date": "2025.06.25",
      "emotion": "이완과 침체",
      "situation": "일상 및 여가"
    }
  },
  {
    "id": "user036_20250728115553_36",
    "document": "인생의 방향에 대해 확신이 서지 않는다. 내가 올바른 길을 가고 있는 건지 의문이 든다.",
    "metadata": {
      "user_id": "user036",
      "date": "2025.06.24",
      "emotion": "혼란과 의심",
      "situation": "내면 활동 및 감정"
    }
  },
  {
    "id": "user037_20250728115553_37",
    "document": "오케스트라 공연을 보며 음악의 아름다움에 완전히 빠져들었다. 예술의 힘이 이런 것이구나 싶었다.",
    "metadata": {
      "user_id": "user037",
      "date": "2025.06.23",
      "emotion": "경이와 압도",
      "situation": "특별한 날과 사건"
    }
  },
  {
    "id": "user038_20250728115553_38",
    "document": "보너스를 받아서 가족들과 맛있는 저녁을 먹을 수 있었다. 열심히 일한 보람이 있다.",
    "metadata": {
      "user_id": "user038",
      "date": "2025.06.22",
      "emotion": "긍정적 감정",
      "situation": "경제 및 소비생활"
    }
  },
  {
    "id": "user039_20250728115553_39",
    "document": "갑작스런 병원 입원으로 모든 계획이 틀어져서 불안하다. 언제 퇴원할 수 있을지 모르겠다.",
    "metadata": {
      "user_id": "user039",
      "date": "2025.06.21",
      "emotion": "두려움과 공포",
      "situation": "건강 및 의료"
    }
  },
  {
    "id": "user040_20250728115553_40",
    "document": "온라인 게임에서 다른 플레이어들과 싸웠는데, 계속 생각나서 잠이 안 온다.",
    "metadata": {
      "user_id": "user040",
      "date": "2025.06.20",
      "emotion": "불안과 긴장",
      "situation": "디지털 및 온라인 활동"
    }
  },
  {
    "id": "user041_20250728115553_41",
    "document": "친구 앞에서 창피한 실수를 해서 얼굴이 빨개졌다. 나는 왜 이렇게 어리석을까 싶다.",
    "metadata": {
      "user_id": "user041",
      "date": "2025.06.19",
      "emotion": "수치와 자책",
      "situation": "인간관계"
    }
  },
  {
    "id": "user042_20250728115553_42",
    "document": "어릴 적 키우던 강아지가 생각나서 눈물이 났다. 그때는 정말 행복했는데.",
    "metadata": {
      "user_id": "user042",
      "date": "2025.06.18",
      "emotion": "그리움과 아쉬움",
      "situation": "내면 활동 및 감정"
    }
  },
  {
    "id": "user043_20250728115553_43",
    "document": "새로운 창작 프로젝트를 시작하고 싶어서 설렌다. 이번에는 정말 멋진 작품을 만들어보고 싶다.",
    "metadata": {
      "user_id": "user043",
      "date": "2025.06.17",
      "emotion": "동기와 욕구",
      "situation": "창작과 성장"
    }
  },
  {
    "id": "user044_20250728115553_44",
    "document": "동아리 모임에서 새로운 사람들과 친해질 수 있어서 기뻤다. 좋은 인연들을 만난 것 같다.",
    "metadata": {
      "user_id": "user044",
      "date": "2025.06.16",
      "emotion": "사회적 관계 감정",
      "situation": "인간관계"
    }
  },
  {
    "id": "user045_20250728115553_45",
    "document": "온종일 침대에 누워서 아무것도 하지 않았다. 뭔가 무기력하고 에너지가 없다.",
    "metadata": {
      "user_id": "user045",
      "date": "2025.06.15",
      "emotion": "이완과 침체",
      "situation": "일상 및 여가"
    }
  },
  {
    "id": "user046_20250728115553_46",
    "document": "새로운 업무를 맡았는데 너무 복잡해서 어디서부터 시작해야 할지 모르겠다.",
    "metadata": {
      "user_id": "user046",
      "date": "2025.06.14",
      "emotion": "혼란과 의심",
      "situation": "업무 및 학습"
    }
  },
  {
    "id": "user047_20250728115553_47",
    "document": "미술관에서 명화를 직접 보니까 감동이 밀려왔다. 화가의 열정이 그대로 전해지는 것 같았다.",
    "metadata": {
      "user_id": "user047",
      "date": "2025.06.13",
      "emotion": "경이와 압도",
      "situation": "특별한 날과 사건"
    }
  },
  {
    "id": "user048_20250728115553_48",
    "document": "용돈을 모아서 원하던 물건을 샀는데 너무 만족스럽다. 저축한 보람이 있다.",
    "metadata": {
      "user_id": "user048",
      "date": "2025.06.12",
      "emotion": "긍정적 감정",
      "situation": "경제 및 소비생활"
    }
  },
  {
    "id": "user049_20250728115553_49",
    "document": "갑작스런 복통으로 병원에 갔는데, 큰 병이면 어떡하지 싶어서 무서웠다.",
    "metadata": {
      "user_id": "user049",
      "date": "2025.06.11",
      "emotion": "두려움과 공포",
      "situation": "건강 및 의료"
    }
  },
  {
    "id": "user050_20250728115553_50",
    "document": "온라인 강의를 듣는데 집중이 안 돼서 자꾸 딴 생각이 난다. 제대로 공부할 수 있을까 걱정된다.",
    "metadata": {
      "user_id": "user050",
      "date": "2025.06.10",
      "emotion": "불안과 긴장",
      "situation": "디지털 및 온라인 활동"
    }
  },
  {
    "id": "user051_20250728115553_51",
    "document": "회의에서 틀린 답을 말해서 모든 사람들이 쳐다봤다. 땅에 구멍이 뚫렸으면 좋겠다는 생각이 들었다.",
    "metadata": {
      "user_id": "user051",
      "date": "2025.06.09",
      "emotion": "수치와 자책",
      "situation": "업무 및 학습"
    }
  },
  {
    "id": "user052_20250728115553_52",
    "document": "대학 시절 함께했던 동기들이 그립다. 그때는 미래에 대한 걱정 없이 함께 웃을 수 있었는데.",
    "metadata": {
      "user_id": "user052",
      "date": "2025.06.08",
      "emotion": "그리움과 아쉬움",
      "situation": "인간관계"
    }
  },
  {
    "id": "user053_20250728115553_53",
    "document": "새로운 취미로 사진을 배우고 싶다는 생각이 든다. 아름다운 순간들을 기록하고 싶다.",
    "metadata": {
      "user_id": "user053",
      "date": "2025.06.07",
      "emotion": "동기와 욕구",
      "situation": "창작과 성장"
    }
  },
  {
    "id": "user054_20250728115553_54",
    "document": "결혼식에서 친구의 행복한 모습을 보니까 나도 덩달아 기뻤다. 좋은 사람과 만나서 다행이다.",
    "metadata": {
      "user_id": "user054",
      "date": "2025.06.06",
      "emotion": "사회적 관계 감정",
      "situation": "특별한 날과 사건"
    }
  },
  {
    "id": "user055_20250728115553_55",
    "document": "요가 수업을 들으며 마음의 평온을 찾았다. 명상하는 시간이 정말 소중하다.",
    "metadata": {
      "user_id": "user055",
      "date": "2025.06.05",
      "emotion": "이완과 침체",
      "situation": "일상 및 여가"
    }
  },
  {
    "id": "user056_20250728115553_56",
    "document": "새로운 기술 트렌드를 따라가기 힘들어서 혼란스럽다. 내가 뒤처지는 건 아닐까 의심된다.",
    "metadata": {
      "user_id": "user056",
      "date": "2025.06.04",
      "emotion": "혼란과 의심",
      "situation": "업무 및 학습"
    }
  },
  {
    "id": "user057_20250728115553_57",
    "document": "천체관측을 하며 우주의 광활함을 느꼈다. 인간이 얼마나 작은 존재인지 깨달았다.",
    "metadata": {
      "user_id": "user057",
      "date": "2025.06.03",
      "emotion": "경이와 압도",
      "situation": "일상 및 여가"
    }
  },
  {
    "id": "user058_20250728115553_58",
    "document": "장보기를 하며 필요한 것들을 사니까 마음이 든든하다. 집을 잘 꾸려나가고 있는 것 같다.",
    "metadata": {
      "user_id": "user058",
      "date": "2025.06.02",
      "emotion": "긍정적 감정",
      "situation": "경제 및 소비생활"
    }
  },
  {
    "id": "user059_20250728115553_59",
    "document": "예방접종을 맞으러 가는데 주사가 무서워서 떨린다. 어릴 때부터 주사를 싫어했다.",
    "metadata": {
      "user_id": "user059",
      "date": "2025.06.01",
      "emotion": "두려움과 공포",
      "situation": "건강 및 의료"
    }
  },
  {
    "id": "user060_20250728115553_60",
    "document": "새로운 앱을 사용하는데 인터페이스가 복잡해서 스트레스받는다. 왜 이렇게 어렵게 만들었을까.",
    "metadata": {
      "user_id": "user060",
      "date": "2025.05.31",
      "emotion": "불안과 긴장",
      "situation": "디지털 및 온라인 활동"
    }
  },
  {
    "id": "user061_20250728115553_61",
    "document": "패션에 대한 센스가 없어서 늘 자신감이 부족하다. 다른 사람들은 어떻게 그렇게 잘 입을까.",
    "metadata": {
      "user_id": "user061",
      "date": "2025.05.30",
      "emotion": "수치와 자책",
      "situation": "일상 및 여가"
    }
  },
  {
    "id": "user062_20250728115553_62",
    "document": "고향에 있는 할머니가 보고 싶다. 코로나 때문에 오랫동안 못 뵙고 있어서 마음이 아프다.",
    "metadata": {
      "user_id": "user062",
      "date": "2025.05.29",
      "emotion": "그리움과 아쉬움",
      "situation": "인간관계"
    }
  },
  {
    "id": "user063_20250728115553_63",
    "document": "건강한 식습관을 만들고 싶어서 요리를 배우기 시작했다. 몸에 좋은 음식을 직접 만들어 먹고 싶다.",
    "metadata": {
      "user_id": "user063",
      "date": "2025.05.28",
      "emotion": "동기와 욕구",
      "situation": "건강 및 의료"
    }
  },
  {
    "id": "user064_20250728115553_64",
    "document": "회사 워크샵에서 동료들과 협력하며 문제를 해결하는 과정이 즐거웠다. 팀워크의 힘을 느꼈다.",
    "metadata": {
      "user_id": "user064",
      "date": "2025.05.27",
      "emotion": "사회적 관계 감정",
      "situation": "업무 및 학습"
    }
  },
  {
    "id": "user065_20250728115553_65",
    "document": "주말에 아무 계획 없이 집에서 쉬는 것도 나쁘지 않다. 때로는 이런 여유가 필요하다.",
    "metadata": {
      "user_id": "user065",
      "date": "2025.05.26",
      "emotion": "이완과 침체",
      "situation": "일상 및 여가"
    }
  },
  {
    "id": "user066_20250728115553_66",
    "document": "인생의 목표가 무엇인지 확실하지 않아서 방황하고 있다. 나는 무엇을 위해 살고 있는 걸까.",
    "metadata": {
      "user_id": "user066",
      "date": "2025.05.25",
      "emotion": "혼란과 의심",
      "situation": "내면 활동 및 감정"
    }
  },
  {
    "id": "user067_20250728115553_67",
    "document": "도서관에서 우연히 발견한 책이 너무 감동적이었다. 작가의 통찰력에 완전히 빠져들었다.",
    "metadata": {
      "user_id": "user067",
      "date": "2025.05.24",
      "emotion": "경이와 압도",
      "situation": "창작과 성장"
    }
  },
  {
    "id": "user068_20250728115553_68",
    "document": "투자했던 주식이 올라서 수익이 났다. 조금이라도 경제적 여유가 생겨서 기분이 좋다.",
    "metadata": {
      "user_id": "user068",
      "date": "2025.05.23",
      "emotion": "긍정적 감정",
      "situation": "경제 및 소비생활"
    }
  },
  {
    "id": "user069_20250728115553_69",
    "document": "치과 치료를 받아야 하는데 무서워서 계속 미루고 있다. 아프면 어떡하지 싶어서 걱정된다.",
    "metadata": {
      "user_id": "user069",
      "date": "2025.05.22",
      "emotion": "두려움과 공포",
      "situation": "건강 및 의료"
    }
  },
  {
    "id": "user070_20250728115553_70",
    "document": "온라인 회의에서 마이크가 안 켜져서 당황했다. 기술적인 문제로 스트레스받는 일이 많다.",
    "metadata": {
      "user_id": "user070",
      "date": "2025.05.21",
      "emotion": "불안과 긴장",
      "situation": "디지털 및 온라인 활동"
    }
  },
  {
    "id": "user071_20250728115553_71",
    "document": "친구들과의 약속에 늦어서 미안했다. 시간 관리를 못하는 내 자신이 한심하다.",
    "metadata": {
      "user_id": "user071",
      "date": "2025.05.20",
      "emotion": "수치와 자책",
      "situation": "인간관계"
    }
  },
  {
    "id": "user072_20250728115553_72",
    "document": "학창시절 선생님이 떠올라서 연락을 드리고 싶다. 그때 받은 가르침이 아직도 도움이 된다.",
    "metadata": {
      "user_id": "user072",
      "date": "2025.05.19",
      "emotion": "그리움과 아쉬움",
      "situation": "내면 활동 및 감정"
    }
  },
  {
    "id": "user073_20250728115553_73",
    "document": "새로운 기술을 익혀서 업무 효율을 높이고 싶다. 더 전문적인 능력을 갖추고 싶다는 욕구가 강하다.",
    "metadata": {
      "user_id": "user073",
      "date": "2025.05.18",
      "emotion": "동기와 욕구",
      "situation": "업무 및 학습"
    }
  },
  {
    "id": "user074_20250728115553_74",
    "document": "새로 이사한 동네에서 이웃들과 인사를 나누니까 따뜻한 마음이 들었다. 좋은 사람들을 만난 것 같다.",
    "metadata": {
      "user_id": "user074",
      "date": "2025.05.17",
      "emotion": "사회적 관계 감정",
      "situation": "인간관계"
    }
  },
  {
    "id": "user075_20250728115553_75",
    "document": "온천에서 목욕하며 완전히 릴렉스했다. 몸과 마음의 피로가 모두 풀리는 것 같았다.",
    "metadata": {
      "user_id": "user075",
      "date": "2025.05.16",
      "emotion": "이완과 침체",
      "situation": "일상 및 여가"
    }
  },
  {
    "id": "user076_20250728115553_76",
    "document": "새로운 프로젝트의 방향성에 대해 확신이 서지 않는다. 이게 올바른 선택인지 계속 의심된다.",
    "metadata": {
      "user_id": "user076",
      "date": "2025.05.15",
      "emotion": "혼란과 의심",
      "situation": "업무 및 학습"
    }
  },
  {
    "id": "user077_20250728115553_77",
    "document": "발레 공연을 보며 무용수들의 우아한 움직임에 감탄했다. 예술의 아름다움에 완전히 빠져들었다.",
    "metadata": {
      "user_id": "user077",
      "date": "2025.05.14",
      "emotion": "경이와 압도",
      "situation": "특별한 날과 사건"
    }
  },
  {
    "id": "user078_20250728115553_78",
    "document": "아르바이트로 번 돈으로 가족에게 선물을 사드렸다. 부모님이 좋아하시는 모습을 보니 뿌듯했다.",
    "metadata": {
      "user_id": "user078",
      "date": "2025.05.13",
      "emotion": "긍정적 감정",
      "situation": "경제 및 소비생활"
    }
  },
  {
    "id": "user079_20250728115553_79",
    "document": "수술을 앞두고 있어서 무섭고 불안하다. 마취에서 깨어날 수 있을까 하는 생각이 든다.",
    "metadata": {
      "user_id": "user079",
      "date": "2025.05.12",
      "emotion": "두려움과 공포",
      "situation": "건강 및 의료"
    }
  },
  {
    "id": "user080_20250728115553_80",
    "document": "새로운 소셜미디어 플랫폼을 사용하는데 복잡해서 적응이 안 된다. 젊은 사람들만 쉽게 쓰는 것 같다.",
    "metadata": {
      "user_id": "user080",
      "date": "2025.05.11",
      "emotion": "불안과 긴장",
      "situation": "디지털 및 온라인 활동"
    }
  },
  {
    "id": "user081_20250728115553_81",
    "document": "운동을 시작했는데 체력이 너무 부족해서 창피하다. 다른 사람들에 비해 너무 못하는 것 같다.",
    "metadata": {
      "user_id": "user081",
      "date": "2025.05.10",
      "emotion": "수치와 자책",
      "situation": "건강 및 의료"
    }
  },
  {
    "id": "user082_20250728115553_82",
    "document": "어릴 적 가족여행을 갔던 바닷가가 그립다. 그때는 모든 게 새롭고 신기했는데.",
    "metadata": {
      "user_id": "user082",
      "date": "2025.05.09",
      "emotion": "그리움과 아쉬움",
      "situation": "일상 및 여가"
    }
  },
  {
    "id": "user083_20250728115553_83",
    "document": "새로운 언어를 배워서 외국인 친구들과 대화하고 싶다. 다른 문화를 이해하고 싶은 마음이 크다.",
    "metadata": {
      "user_id": "user083",
      "date": "2025.05.08",
      "emotion": "동기와 욕구",
      "situation": "창작과 성장"
    }
  },
  {
    "id": "user084_20250728115553_84",
    "document": "동호회 모임에서 같은 취미를 가진 사람들과 만나니까 즐거웠다. 서로의 경험을 나누는 시간이 소중했다.",
    "metadata": {
      "user_id": "user084",
      "date": "2025.05.07",
      "emotion": "사회적 관계 감정",
      "situation": "일상 및 여가"
    }
  },
  {
    "id": "user085_20250728115553_85",
    "document": "카페에서 책을 읽으며 조용한 시간을 보냈다. 이런 평온한 순간들이 정말 소중하다.",
    "metadata": {
      "user_id": "user085",
      "date": "2025.05.06",
      "emotion": "이완과 침체",
      "situation": "일상 및 여가"
    }
  },
  {
    "id": "user086_20250728115553_86",
    "document": "새로운 분야로 이직을 고려하고 있는데, 내가 잘할 수 있을지 의문이다. 너무 큰 모험은 아닐까.",
    "metadata": {
      "user_id": "user086",
      "date": "2025.05.05",
      "emotion": "혼란과 의심",
      "situation": "업무 및 학습"
    }
  },
  {
    "id": "user087_20250728115553_87",
    "document": "처음 본 거대한 폭포 앞에서 자연의 위력에 압도당했다. 인간이 얼마나 작은 존재인지 깨달았다.",
    "metadata": {
      "user_id": "user087",
      "date": "2025.05.04",
      "emotion": "경이와 압도",
      "situation": "일상 및 여가"
    }
  },
  {
    "id": "user088_20250728115553_88",
    "document": "용돈을 모아서 원하던 책을 샀다. 작은 목표라도 달성하니까 기분이 좋다.",
    "metadata": {
      "user_id": "user088",
      "date": "2025.05.03",
      "emotion": "긍정적 감정",
      "situation": "경제 및 소비생활"
    }
  },
  {
    "id": "user089_20250728115553_89",
    "document": "병원에서 암 검사를 받는다고 하니까 무서워서 잠이 안 온다. 결과가 나쁘면 어떡하지.",
    "metadata": {
      "user_id": "user089",
      "date": "2025.05.02",
      "emotion": "두려움과 공포",
      "situation": "건강 및 의료"
    }
  },
  {
    "id": "user090_20250728115553_90",
    "document": "온라인 쇼핑몰에서 환불 요청을 했는데 처리가 안 되어서 짜증난다. 고객센터도 연결이 안 된다.",
    "metadata": {
      "user_id": "user090",
      "date": "2025.05.01",
      "emotion": "불안과 긴장",
      "situation": "디지털 및 온라인 활동"
    }
  },
  {
    "id": "user091_20250728115553_91",
    "document": "모든 사람 앞에서 발표할 때 목소리가 떨렸다. 나는 왜 이렇게 자신감이 없을까 자책하게 된다.",
    "metadata": {
      "user_id": "user091",
      "date": "2025.04.30",
      "emotion": "수치와 자책",
      "situation": "업무 및 학습"
    }
  },
  {
    "id": "user092_20250728115553_92",
    "document": "군대에 간 친구가 보고 싶다. 함께 놀던 시절이 그리워서 편지를 써보려고 한다.",
    "metadata": {
      "user_id": "user092",
      "date": "2025.04.29",
      "emotion": "그리움과 아쉬움",
      "situation": "인간관계"
    }
  },
  {
    "id": "user093_20250728115553_93",
    "document": "새로운 직업을 가지고 싶어서 자격증 공부를 시작했다. 더 나은 미래를 위해 열심히 해야겠다.",
    "metadata": {
      "user_id": "user093",
      "date": "2025.04.28",
      "emotion": "동기와 욕구",
      "situation": "업무 및 학습"
    }
  },
  {
    "id": "user094_20250728115553_94",
    "document": "새로운 직장에서 동료들이 친절하게 도와줘서 고마웠다. 좋은 팀에 들어온 것 같아서 안심된다.",
    "metadata": {
      "user_id": "user094",
      "date": "2025.04.27",
      "emotion": "사회적 관계 감정",
      "situation": "업무 및 학습"
    }
  },
  {
    "id": "user095_20250728115553_95",
    "document": "주말에 산책하며 자연을 감상했다. 바쁜 일상에서 잠시나마 벗어날 수 있어서 좋았다.",
    "metadata": {
      "user_id": "user095",
      "date": "2025.04.26",
      "emotion": "이완과 침체",
      "situation": "일상 및 여가"
    }
  },
  {
    "id": "user096_20250728115553_96",
    "document": "내 인생의 방향에 대해 확신이 서지 않는다. 지금 하고 있는 일이 정말 맞는 길일까 의문이 든다.",
    "metadata": {
      "user_id": "user096",
      "date": "2025.04.25",
      "emotion": "혼란과 의심",
      "situation": "내면 활동 및 감정"
    }
  },
  {
    "id": "user097_20250728115553_97",
    "document": "처음 본 오로라의 아름다움에 말문이 막혔다. 자연이 만들어내는 신비로운 광경에 완전히 빠져들었다.",
    "metadata": {
      "user_id": "user097",
      "date": "2025.04.24",
      "emotion": "경이와 압도",
      "situation": "특별한 날과 사건"
    }
  },
  {
    "id": "user098_20250728115553_98",
    "document": "부모님께 용돈을 드릴 수 있게 되어서 기쁘다. 그동안 받기만 했는데 이제는 보답할 수 있어서 뿌듯하다.",
    "metadata": {
      "user_id": "user098",
      "date": "2025.04.23",
      "emotion": "긍정적 감정",
      "situation": "경제 및 소비생활"
    }
  },
  {
    "id": "user099_20250728115553_99",
    "document": "응급실에 실려갔던 경험이 트라우마가 되어서 아직도 무섭다. 갑작스런 응급상황이 또 올까 봐 불안하다.",
    "metadata": {
      "user_id": "user099",
      "date": "2025.04.22",
      "emotion": "두려움과 공포",
      "situation": "건강 및 의료"
    }
  },
  {
    "id": "user100_20250728115553_100",
    "document": "새로운 글쓰기 플랫폼에 첫 글을 올렸는데, 사람들의 반응이 어떨지 궁금하면서도 걱정된다.",
    "metadata": {
      "user_id": "user100",
      "date": "2025.04.21",
      "emotion": "불안과 긴장",
      "situation": "디지털 및 온라인 활동"
    }
  }
]