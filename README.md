# AI 기반 다목적 챗봇  
<h3>ChatGPT API를 이용해 다양한 기능을 제공하는 AI 챗봇 시스템</h3>  
<br/>

## 📝 작품소개  
OpenAI의 ChatGPT API, Whisper API, LangChain, Twitter API를 활용하여 다양한 기능을 제공하는 다목적 AI 챗봇 시스템을 개발하였습니다. <br>
챗봇은 자연어로 사용자와 상호작용하며, 트윗 자동 생성, 뉴스 기사 자동 생성, 음성 전사 및 번역, PDF 데이터 추출 및 시각화 등의 다양한 기능을 제공합니다.

<br>

## 🌁 주요 기능  
- **트윗 자동 생성 봇**  
  - Twitter API를 이용하여 사용자의 입력이나 특정 키워드를 기반으로 자동으로 글감(트윗)을 생성
  - 실시간으로 트윗을 생성하여 사용자와 상호작용

<table>
  <tr>
    <td align="center" width="50%">
      <img src="https://github.com/user-attachments/assets/c64560d7-e217-406b-a2dc-2f619d108375" width="100%" />
    </td>
    <td align="center" width="50%">
      <img src="https://github.com/user-attachments/assets/5285d6b4-427e-4c4c-b516-8ef065206e0c" width="100%" />
    </td>
  </tr>
  <tr>
    <td align="center" colspan="2">
      <p align="center">temperature=0으로 설정</p>
    </td>
  </tr>
</table>

<table>
  <tr>
    <td align="center" width="50%">
      <img src="https://github.com/user-attachments/assets/c7673b33-d5af-4213-9e7b-2fb9f0e1b2b1" width="100%" />
    </td>
    <td align="center" width="50%">
      <img src="https://github.com/user-attachments/assets/d0ff3066-d479-4700-bb41-94532df44104" width="100%" />
    </td>
  </tr>
  <tr>
    <td align="center" colspan="2">
      <p align="center">어조 조절(낙천적인 성격, '~인 것이다'로 끝맺음</p>
    </td>
  </tr>
</table>
<br/>

- **LangChain을 이용한 뉴스 기사 자동 생성 봇**  
  - LangChain 프레임워크를 사용하여 사용자가 입력한 주제에 대한 뉴스 기사를 자동으로 생성
  - 주제에 맞는 최신 뉴스 기사를 작성하여 제공

<table>
  <tr>
    <td align="center" width="50%">
      <img src="https://github.com/user-attachments/assets/52092635-365a-4b01-8ff8-47aa2e244545" width="100%" />
    </td>
    <td align="center" width="50%">
      <img src="https://github.com/user-attachments/assets/e4238c53-e855-4e39-8623-88dc488cf75a" width="100%" />
    </td>
  </tr>
  <tr>
    <td align="center" style="border: none;">
      <p align="center">최신 정보를 포함한 뉴스 기사 생성 <br>[입력: M4를 탑재한 아이패드 프로]</p>
    </td>
    <td align="center" style="border: none;">
      <p align="center">최신 음악 창작 AI 추천 <br>[입력: Recommend the latest music creation AI service]</p>
    </td>
  </tr>
</table>

<br>

- **Whisper API를 이용한 음성 처리 시스템**  
  - 사용자가 음성 파일을 업로드하면, Whisper API를 사용하여 음성을 텍스트로 전사  
  - 전사된 텍스트를 원하는 언어로 번역하고 요약하는 시스템
 
<table>
  <tr>
    <td align="center" width="50%">
      <img src="https://github.com/user-attachments/assets/03968579-0dc9-45f7-b3ea-a6f589738c0a" width="100%" />
    </td>
  </tr>
  <tr>
    <td align="center" colspan="2">
      <p align="center">음성 파일 전사</p>
    </td>
  </tr>
</table>
<table>
  <tr>
    <td align="center" width="50%">
      <img src="https://github.com/user-attachments/assets/da6465b7-b54e-44d4-a148-783a0cc45f46" width="100%" />
    </td>
  </tr>
  <tr>
    <td align="center" colspan="2">
      <p align="center">SRT 형식(자막)으로 출력</p>
    </td>
  </tr>
</table>
<table>
  <tr>
    <td align="center" width="50%">
      <img src="https://github.com/user-attachments/assets/5279d484-40c8-4350-ba5a-11f47fa2eca0" width="100%" />
    </td>
  </tr>
  <tr>
    <td align="center" colspan="2">
      <p align="center">GPT를 이용한 전사 내용 요약</p>
    </td>
  </tr>
</table>
<table>
  <tr>
    <td align="center" width="50%">
      <img src="https://github.com/user-attachments/assets/327a99ff-a8df-418d-a13a-d6b60fb4e900" width="100%" />
    </td>
  </tr>
  <tr>
    <td align="center" colspan="2">
      <p align="center">한국어 음성을 영어로 변역하여 전사</p>
    </td>
  </tr>
</table>
<table>
  <tr>
    <td align="center" width="50%">
      <img src="https://github.com/user-attachments/assets/d6c47050-858b-446e-b277-81aa4659dd1e" width="100%" />
    </td>
  </tr>
  <tr>
    <td align="center" colspan="2">
      <p align="center">영어로 변역하면서 요약</p>
    </td>
  </tr>
</table>

<br>

- **PDF 문서 데이터 추출 및 시각화 시스템**  
  - 사용자가 업로드한 PDF 파일에서 텍스트 및 구조화된 데이터를 추출  
  - 추출된 데이터를 시각화하여 사용자에게 유용한 정보를 제공

<br/>

## 🔧 Stack  
**Language**  
- Python  

**Libraries & APIs**  
- OpenAI API (ChatGPT API)  
- Whisper API  
- LangChain  
- Twitter API  

<br/>

## 💡 기대효과  
- **사용자 생산성 향상**: 트윗 생성, 뉴스 기사 작성, 음성 전사 등의 반복적인 작업을 빠르게 처리
- **정보 접근성 개선**: PDF 데이터 추출 및 시각화를 통해 중요한 인사이트를 빠르게 파악 <br>
                       음성 파일의 전사 및 번역 기능으로 언어 장벽을 낮춤
- **창의성 및 아이디어 지원**: 트윗 자동 생성 기능을 통해 소셜 미디어 콘텐츠 제작 아이디어를 얻을 수 있음 <br>
                              뉴스 기사 자동 생성 기능으로 다양한 주제에 대한 글쓰기 영감을 얻을 수 있음
- **지속적인 학습**: API와 최신 AI 모델을 활용함으로써 시스템의 성능을 지속적으로 향상시킬 수 있음

<br/>

## 🙋‍♂️ Developer  
| Fullstack |  
| :--------: |  
| [김가은](https://github.com/gaeunamy) |
