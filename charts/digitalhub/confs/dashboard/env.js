{{ if .Values.dashboard.oidc.enabled -}}
window.env = {"VITE_OIDC_CONFIG":JSON.stringify({"accessTokenExpiringNotificationTime": "3570", "authority": "{{ .Values.dashboard.oidc.config.issuer }}", "clientId": "{{ .Values.dashboard.oidc.audience.clientId }}", "redirectUri": "http://{{ include "digitalhub.oidcDashboardEndpoint" . }}/oidc-callback", "responseType": "code", "scope": "openid profile email", "automaticSilentRenew": "false", "automaticSilentSignin": "false", "post_logout_redirect_uri": "http://{{ include "digitalhub.oidcDashboardEndpoint" . }}"}), "VITE_PLATFORM_TITLE": "OltreAI", "VITE_PLATFORM_VERSION": "0.8"}
{{- else -}}
window.env = {"VITE_OIDC_CONFIG": null, "VITE_PLATFORM_TITLE": "OltreAI", "VITE_PLATFORM_VERSION": "0.8"}
{{- end }}
