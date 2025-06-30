## 장고 인증 처리 뷰
- LoginView
  - 로그인 폼을 처리하고 사용자를 로그인 시킴
- LogoutView
  - 사용자를 로그아웃 시킴
- PasswordChangeView
  - 사용자의 패스워드를 변경하는 폼을 처리한다.
- PasswordChangeDoneView
  - 성공적인 패스워드 변경 후 사용자가 리디렉션되는 성공 뷰
- PasswordResetDoneView
  - 사용자에게 패스워드 재설정 링크가 포함된 이메일이 전송되었음을 알림
- PasswordResetConfirmView
  - 사용자가 새로운 패스워드를 설정할 수 있다.
- PasswordResetCompleteView
  - 사용자가 패스워드를 성공적으로 재설정한 후 리디렉션 되는 성공 뷰

### 장고 기본 로그인 방식
Django는

별도 커스터마이징을 하지 않는 한 기본적으로 “세션 기반 인증(Session Authentication)”
을 사용해.

즉:
django.contrib.sessions 와 django.contrib.auth 앱을 통해
사용자가 login() 하면 서버에서 세션 데이터를 만들고,
사용자 브라우저에는 sessionid 라는 쿠키를 내려보냄.

