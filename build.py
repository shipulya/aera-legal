#!/usr/bin/env python3
"""Собирает index.html с политикой конфиденциальности Aera на восьми языках.

Страница публикуется из отдельного публичного репозитория shipulya/aera-legal
(GitHub Pages): основной репозиторий приватный, а бесплатный Pages работает
только с публичными. Меняешь текст или контакт — правь этот файл и запускай
`python3 legal/build.py`, затем публикуй (см. CLAUDE.md, раздел «Политика»).

Все языки лежат в одном HTML: без JavaScript виден английский, скрипт
переключает язык по ?lang=, по языку браузера или по кнопкам сверху.
Приложение открывает страницу с ?lang=<язык интерфейса>.
"""

from html import escape
from pathlib import Path

UPDATED_ISO = "2026-09-27"

# Контакт для связи: почта разработчика (показывается на обеих страницах)
CONTACT_EMAIL = "shipulya.gv@gmail.com"
CONTACT_URL = f"mailto:{CONTACT_EMAIL}"

LANGS = [
    ("ru", "Русский"), ("en", "English"), ("es", "Español"), ("pt-BR", "Português"),
    ("de", "Deutsch"), ("fr", "Français"), ("it", "Italiano"), ("ja", "日本語"),
]

# Для каждого языка: заголовок, «Обновлено», вступление, разделы (заголовок, абзацы).
# {contact} заменяется ссылкой для связи.
T = {
"ru": {
 "title": "Политика конфиденциальности Aera",
 "updated": "Обновлено 27 сентября 2026 г.",
 "lead": "Aera — приложение для учёта личных финансов. Коротко: мы не собираем ваши данные. У Aera нет серверов, аккаунтов и регистрации, и приложение не передаёт ваши данные ни нам, ни третьим лицам.",
 "sections": [
  ("Какие данные хранит приложение", ["Кошельки, операции, категории, бюджеты, цели, долги, списки покупок, шаблоны, прикреплённые фото чеков и настройки. Всё это хранится только на вашем устройстве, в защищённом хранилище приложения. Эти данные доступны самой Aera, её виджетам и командам Siri на этом устройстве — и больше никому."]),
  ("Что мы собираем", ["Ничего. В Aera нет аналитики, рекламы, отслеживания, отчётов о сбоях и сторонних SDK. Приложение не подключается к интернету, кроме покупок через App Store, которые обрабатывает Apple."]),
  ("Face ID и PIN-код", ["Face ID и Touch ID обрабатывает iOS: приложение получает только ответ «подтверждено» или «нет» и никогда не видит биометрические данные. PIN-код не хранится в открытом виде: на устройстве, в защищённой Связке ключей iOS, лежит только его стойкий хеш с солью. В резервные копии он не попадает."]),
  ("Фотографии", ["Aera получает только те фото чеков, которые вы сами выберете в системном окне выбора. Они хранятся внутри приложения и никуда не отправляются."]),
  ("Уведомления", ["Напоминания и сводки — локальные уведомления: они создаются и показываются на устройстве, без серверов push-уведомлений."]),
  ("Покупки Aera Pro", ["Подписку и покупку Aera Pro обрабатывает Apple через App Store. Приложение узнаёт только, активна ли у вас Aera Pro, и не видит ваших платёжных данных. На оплату распространяется политика конфиденциальности Apple."]),
  ("Резервные копии и экспорт", ["Файлы резервной копии и CSV создаются только по вашей команде и сохраняются туда, куда вы укажете, — например, в «Файлы» или iCloud Drive. Дальше на них распространяются правила выбранного сервиса. Если в iOS включено резервное копирование устройства в iCloud, данные приложения могут попасть в него по правилам Apple."]),
  ("Удаление данных", ["Отдельные записи можно удалить в приложении. Если удалить Aera с устройства, все её данные удаляются вместе с ней."]),
  ("Дети", ["Мы не собираем данных ни у кого, в том числе у детей."]),
  ("Изменения политики", ["Если политика изменится, мы обновим эту страницу и дату вверху."]),
  ("Связь", ["Вопросы о конфиденциальности присылайте на почту {contact}. Ответы на частые вопросы — на странице {support}."]),
 ],
},
"en": {
 "title": "Aera Privacy Policy",
 "updated": "Updated September 27, 2026",
 "lead": "Aera is a personal finance app. In short: we don’t collect your data. Aera has no servers, accounts or sign-up, and the app never sends your data to us or to anyone else.",
 "sections": [
  ("What the app stores", ["Wallets, transactions, categories, budgets, goals, debts, shopping lists, templates, attached receipt photos and settings. All of it is stored only on your device, in the app’s protected storage. It is available to Aera itself and to its widgets and Siri shortcuts on that device — and to no one else."]),
  ("What we collect", ["Nothing. Aera has no analytics, ads, tracking, crash reporting or third-party SDKs. The app does not connect to the internet, except for App Store purchases, which are handled by Apple."]),
  ("Face ID and PIN", ["Face ID and Touch ID are handled by iOS: the app only receives a “confirmed” or “not confirmed” result and never sees biometric data. Your PIN is never stored in plain text: only a strong salted hash is kept on the device, in the protected iOS Keychain. It is not included in backups."]),
  ("Photos", ["Aera only receives the receipt photos you choose yourself in the system photo picker. They are stored inside the app and never sent anywhere."]),
  ("Notifications", ["Reminders and summaries are local notifications: they are created and shown on your device, with no push notification servers."]),
  ("Aera Pro purchases", ["Aera Pro subscriptions and purchases are processed by Apple through the App Store. The app only learns whether Aera Pro is active and never sees your payment details. Payments are covered by Apple’s privacy policy."]),
  ("Backups and export", ["Backup and CSV files are created only when you ask and are saved wherever you choose — for example, in Files or iCloud Drive. From then on, the rules of that service apply. If iCloud device backup is turned on in iOS, app data may be included in it under Apple’s terms."]),
  ("Deleting your data", ["You can delete individual records in the app. Deleting Aera from your device removes all of its data."]),
  ("Children", ["We don’t collect data from anyone, including children."]),
  ("Changes to this policy", ["If this policy changes, we’ll update this page and the date at the top."]),
  ("Contact", ["Send privacy questions to {contact}. Answers to common questions are on the {support} page."]),
 ],
},
"es": {
 "title": "Política de privacidad de Aera",
 "updated": "Actualizada el 27 de septiembre de 2026",
 "lead": "Aera es una app de finanzas personales. En resumen: no recopilamos tus datos. Aera no tiene servidores, cuentas ni registro, y la app nunca envía tus datos ni a nosotros ni a terceros.",
 "sections": [
  ("Qué datos guarda la app", ["Carteras, movimientos, categorías, presupuestos, metas, deudas, listas de compras, plantillas, fotos de tiques adjuntas y ajustes. Todo se guarda solo en tu dispositivo, en el almacenamiento protegido de la app. Solo tienen acceso Aera, sus widgets y sus atajos de Siri en ese dispositivo."]),
  ("Qué recopilamos", ["Nada. Aera no tiene analíticas, publicidad, seguimiento, informes de fallos ni SDK de terceros. La app no se conecta a internet, salvo para las compras en el App Store, que gestiona Apple."]),
  ("Face ID y PIN", ["Face ID y Touch ID los gestiona iOS: la app solo recibe la respuesta «confirmado» o «no confirmado» y nunca ve datos biométricos. El PIN nunca se guarda en texto plano: en el dispositivo, en el llavero protegido de iOS, solo se conserva un hash robusto con sal. No se incluye en las copias de seguridad."]),
  ("Fotos", ["Aera solo recibe las fotos de tiques que tú eliges en el selector de fotos del sistema. Se guardan dentro de la app y no se envían a ningún sitio."]),
  ("Notificaciones", ["Los recordatorios y resúmenes son notificaciones locales: se crean y se muestran en tu dispositivo, sin servidores de notificaciones push."]),
  ("Compras de Aera Pro", ["Las suscripciones y compras de Aera Pro las procesa Apple a través del App Store. La app solo sabe si Aera Pro está activo y nunca ve tus datos de pago. Los pagos se rigen por la política de privacidad de Apple."]),
  ("Copias de seguridad y exportación", ["Los archivos de copia de seguridad y CSV se crean solo cuando tú lo pides y se guardan donde elijas, por ejemplo en Archivos o iCloud Drive. A partir de ahí se aplican las normas de ese servicio. Si la copia de seguridad del dispositivo en iCloud está activada en iOS, los datos de la app pueden incluirse en ella según las condiciones de Apple."]),
  ("Eliminar tus datos", ["Puedes eliminar registros concretos en la app. Si eliminas Aera de tu dispositivo, se eliminan todos sus datos."]),
  ("Menores", ["No recopilamos datos de nadie, tampoco de menores."]),
  ("Cambios en esta política", ["Si esta política cambia, actualizaremos esta página y la fecha de arriba."]),
  ("Contacto", ["Envía tus preguntas sobre privacidad a {contact}. Las respuestas a las dudas frecuentes están en la página de {support}."]),
 ],
},
"pt-BR": {
 "title": "Política de privacidade do Aera",
 "updated": "Atualizada em 27 de setembro de 2026",
 "lead": "O Aera é um app de finanças pessoais. Resumindo: não coletamos seus dados. O Aera não tem servidores, contas nem cadastro, e o app nunca envia seus dados para nós ou para terceiros.",
 "sections": [
  ("Quais dados o app guarda", ["Carteiras, transações, categorias, orçamentos, metas, dívidas, listas de compras, modelos, fotos de notas anexadas e ajustes. Tudo fica armazenado apenas no seu aparelho, no armazenamento protegido do app. Só o Aera, seus widgets e atalhos da Siri nesse aparelho têm acesso."]),
  ("O que coletamos", ["Nada. O Aera não tem análises, anúncios, rastreamento, relatórios de falhas nem SDKs de terceiros. O app não se conecta à internet, exceto para compras na App Store, que são processadas pela Apple."]),
  ("Face ID e PIN", ["O Face ID e o Touch ID são processados pelo iOS: o app recebe apenas a resposta “confirmado” ou “não confirmado” e nunca vê dados biométricos. O PIN nunca é armazenado em texto simples: no aparelho, nas Chaves protegidas do iOS, fica apenas um hash robusto com salt. Ele não é incluído em backups."]),
  ("Fotos", ["O Aera recebe apenas as fotos de notas que você mesmo escolhe no seletor de fotos do sistema. Elas ficam dentro do app e não são enviadas para lugar nenhum."]),
  ("Notificações", ["Lembretes e resumos são notificações locais: são criados e exibidos no seu aparelho, sem servidores de notificações push."]),
  ("Compras do Aera Pro", ["Assinaturas e compras do Aera Pro são processadas pela Apple na App Store. O app só sabe se o Aera Pro está ativo e nunca vê seus dados de pagamento. Os pagamentos seguem a política de privacidade da Apple."]),
  ("Backups e exportação", ["Arquivos de backup e CSV são criados só quando você pede e salvos onde você escolher — por exemplo, no Arquivos ou no iCloud Drive. A partir daí, valem as regras desse serviço. Se o backup do aparelho no iCloud estiver ativado no iOS, os dados do app podem ser incluídos nele conforme os termos da Apple."]),
  ("Exclusão de dados", ["Você pode apagar registros individuais no app. Ao apagar o Aera do aparelho, todos os dados dele são removidos."]),
  ("Crianças", ["Não coletamos dados de ninguém, inclusive de crianças."]),
  ("Alterações nesta política", ["Se esta política mudar, atualizaremos esta página e a data no topo."]),
  ("Contato", ["Envie dúvidas sobre privacidade para {contact}. Respostas às perguntas frequentes estão na página de {support}."]),
 ],
},
"de": {
 "title": "Datenschutzerklärung für Aera",
 "updated": "Aktualisiert am 27. September 2026",
 "lead": "Aera ist eine App für persönliche Finanzen. Kurz gesagt: Wir erheben keine Daten über dich. Aera hat keine Server, keine Benutzerkonten und keine Registrierung, und die App sendet deine Daten weder an uns noch an Dritte.",
 "sections": [
  ("Welche Daten die App speichert", ["Konten, Buchungen, Kategorien, Budgets, Sparziele, Schulden, Einkaufslisten, Vorlagen, angehängte Fotos von Kassenbons und Einstellungen. All das wird nur auf deinem Gerät im geschützten Speicher der App abgelegt. Zugriff haben nur Aera selbst sowie ihre Widgets und Siri-Kurzbefehle auf diesem Gerät."]),
  ("Was wir erheben", ["Nichts. Aera enthält keine Analyse, keine Werbung, kein Tracking, keine Absturzberichte und keine SDKs von Drittanbietern. Die App verbindet sich nicht mit dem Internet – außer für Käufe im App Store, die Apple abwickelt."]),
  ("Face ID und PIN", ["Face ID und Touch ID werden von iOS verarbeitet: Die App erhält nur die Antwort „bestätigt“ oder „nicht bestätigt“ und sieht niemals biometrische Daten. Deine PIN wird nie im Klartext gespeichert: Auf dem Gerät liegt im geschützten iOS-Schlüsselbund nur ein starker, gesalzener Hash. Er ist nicht in Backups enthalten."]),
  ("Fotos", ["Aera erhält nur die Fotos von Kassenbons, die du selbst in der Fotoauswahl des Systems auswählst. Sie werden in der App gespeichert und nirgendwohin gesendet."]),
  ("Mitteilungen", ["Erinnerungen und Bilanzen sind lokale Mitteilungen: Sie werden auf deinem Gerät erstellt und angezeigt, ohne Push-Server."]),
  ("Käufe von Aera Pro", ["Abos und Käufe von Aera Pro wickelt Apple über den App Store ab. Die App erfährt nur, ob Aera Pro aktiv ist, und sieht niemals deine Zahlungsdaten. Für Zahlungen gilt die Datenschutzrichtlinie von Apple."]),
  ("Backups und Export", ["Backup- und CSV-Dateien werden nur auf deinen Wunsch erstellt und dort gespeichert, wo du es festlegst – zum Beispiel in „Dateien“ oder iCloud Drive. Danach gelten die Regeln dieses Dienstes. Ist in iOS das iCloud-Backup des Geräts aktiviert, können App-Daten nach den Bedingungen von Apple darin enthalten sein."]),
  ("Löschen deiner Daten", ["Einzelne Einträge kannst du in der App löschen. Wenn du Aera vom Gerät löschst, werden alle ihre Daten entfernt."]),
  ("Kinder", ["Wir erheben von niemandem Daten, auch nicht von Kindern."]),
  ("Änderungen dieser Erklärung", ["Wenn sich diese Erklärung ändert, aktualisieren wir diese Seite und das Datum oben."]),
  ("Kontakt", ["Fragen zum Datenschutz schickst du an {contact}. Antworten auf häufige Fragen findest du auf der Seite {support}."]),
 ],
},
"fr": {
 "title": "Politique de confidentialité d’Aera",
 "updated": "Mise à jour le 27 septembre 2026",
 "lead": "Aera est une app de finances personnelles. En bref : nous ne collectons pas vos données. Aera n’a ni serveur, ni compte utilisateur, ni inscription, et l’app n’envoie jamais vos données, ni à nous ni à des tiers.",
 "sections": [
  ("Données conservées par l’app", ["Comptes, opérations, catégories, budgets, objectifs, dettes, listes d’achats, modèles, photos de tickets jointes et réglages. Tout est stocké uniquement sur votre appareil, dans l’espace protégé de l’app. Seuls Aera, ses widgets et ses raccourcis Siri sur cet appareil y ont accès."]),
  ("Ce que nous collectons", ["Rien. Aera n’intègre ni analyse, ni publicité, ni suivi, ni rapport de plantage, ni SDK tiers. L’app ne se connecte pas à Internet, sauf pour les achats sur l’App Store, gérés par Apple."]),
  ("Face ID et code PIN", ["Face ID et Touch ID sont gérés par iOS : l’app reçoit seulement la réponse « confirmé » ou « non confirmé » et ne voit jamais de données biométriques. Votre code PIN n’est jamais stocké en clair : seul un hachage robuste et salé est conservé sur l’appareil, dans le trousseau iOS protégé. Il n’est pas inclus dans les sauvegardes."]),
  ("Photos", ["Aera reçoit uniquement les photos de tickets que vous choisissez vous-même dans le sélecteur de photos du système. Elles sont stockées dans l’app et ne sont envoyées nulle part."]),
  ("Notifications", ["Les rappels et bilans sont des notifications locales : ils sont créés et affichés sur votre appareil, sans serveur de notifications push."]),
  ("Achats Aera Pro", ["Les abonnements et achats Aera Pro sont traités par Apple via l’App Store. L’app sait seulement si Aera Pro est actif et ne voit jamais vos informations de paiement. Les paiements relèvent de la politique de confidentialité d’Apple."]),
  ("Sauvegardes et export", ["Les fichiers de sauvegarde et CSV sont créés uniquement à votre demande et enregistrés à l’endroit de votre choix, par exemple dans Fichiers ou iCloud Drive. Les règles de ce service s’appliquent ensuite. Si la sauvegarde iCloud de l’appareil est activée dans iOS, les données de l’app peuvent y être incluses selon les conditions d’Apple."]),
  ("Suppression de vos données", ["Vous pouvez supprimer des éléments dans l’app. Supprimer Aera de votre appareil efface toutes ses données."]),
  ("Enfants", ["Nous ne collectons de données auprès de personne, y compris les enfants."]),
  ("Modifications de cette politique", ["Si cette politique change, nous mettrons à jour cette page et la date en haut."]),
  ("Contact", ["Pour toute question sur la confidentialité, écrivez à {contact}. Les réponses aux questions fréquentes sont sur la page {support}."]),
 ],
},
"it": {
 "title": "Informativa sulla privacy di Aera",
 "updated": "Aggiornata il 27 settembre 2026",
 "lead": "Aera è un’app per le finanze personali. In breve: non raccogliamo i tuoi dati. Aera non ha server, account né registrazione, e l’app non invia mai i tuoi dati né a noi né a terzi.",
 "sections": [
  ("Quali dati conserva l’app", ["Conti, movimenti, categorie, budget, obiettivi, debiti, liste della spesa, modelli, foto degli scontrini allegate e impostazioni. Tutto è salvato solo sul tuo dispositivo, nello spazio protetto dell’app. Vi accedono solo Aera, i suoi widget e i suoi comandi Siri su quel dispositivo."]),
  ("Cosa raccogliamo", ["Niente. Aera non contiene analisi, pubblicità, tracciamento, report sugli arresti anomali né SDK di terze parti. L’app non si collega a Internet, tranne che per gli acquisti sull’App Store, gestiti da Apple."]),
  ("Face ID e PIN", ["Face ID e Touch ID sono gestiti da iOS: l’app riceve solo la risposta «confermato» o «non confermato» e non vede mai dati biometrici. Il PIN non viene mai salvato in chiaro: sul dispositivo, nel portachiavi protetto di iOS, resta solo un hash robusto con salt. Non viene incluso nei backup."]),
  ("Foto", ["Aera riceve solo le foto degli scontrini che scegli tu nel selettore di foto del sistema. Restano nell’app e non vengono inviate da nessuna parte."]),
  ("Notifiche", ["Promemoria e riepiloghi sono notifiche locali: vengono create e mostrate sul tuo dispositivo, senza server di notifiche push."]),
  ("Acquisti di Aera Pro", ["Abbonamenti e acquisti di Aera Pro sono gestiti da Apple tramite l’App Store. L’app sa solo se Aera Pro è attivo e non vede mai i tuoi dati di pagamento. I pagamenti sono regolati dall’informativa sulla privacy di Apple."]),
  ("Backup ed esportazione", ["I file di backup e CSV vengono creati solo su tua richiesta e salvati dove scegli, per esempio in File o iCloud Drive. Da quel momento valgono le regole di quel servizio. Se in iOS è attivo il backup del dispositivo su iCloud, i dati dell’app possono esservi inclusi secondo i termini di Apple."]),
  ("Eliminazione dei dati", ["Puoi eliminare singoli elementi nell’app. Se elimini Aera dal dispositivo, vengono rimossi tutti i suoi dati."]),
  ("Minori", ["Non raccogliamo dati da nessuno, minori compresi."]),
  ("Modifiche a questa informativa", ["Se l’informativa cambia, aggiorneremo questa pagina e la data in alto."]),
  ("Contatti", ["Per domande sulla privacy scrivi a {contact}. Le risposte alle domande frequenti sono nella pagina {support}."]),
 ],
},
"ja": {
 "title": "Aera プライバシーポリシー",
 "updated": "2026年9月27日更新",
 "lead": "Aeraは家計管理アプリです。要点：私たちはあなたのデータを収集しません。Aeraにはサーバー、アカウント、ユーザー登録がなく、アプリがあなたのデータを私たちや第三者に送信することはありません。",
 "sections": [
  ("アプリが保存するデータ", ["口座、取引、カテゴリ、予算、目標、貸し借り、買い物リスト、テンプレート、添付したレシートの写真、設定。これらはすべてあなたのデバイス上の、アプリの保護されたストレージにのみ保存されます。アクセスできるのは、そのデバイス上のAera本体とそのウィジェット、Siriショートカットだけです。"]),
  ("収集する情報", ["ありません。Aeraには分析、広告、トラッキング、クラッシュレポート、サードパーティのSDKは含まれていません。App Storeでの購入（Appleが処理）を除き、アプリはインターネットに接続しません。"]),
  ("Face IDとPIN", ["Face IDとTouch IDはiOSが処理します。アプリが受け取るのは「確認済み」か「未確認」かという結果のみで、生体情報を見ることはありません。PINが平文で保存されることはありません。デバイス上の保護されたiOSキーチェーンに、ソルト付きの強固なハッシュだけが保存され、バックアップには含まれません。"]),
  ("写真", ["Aeraが受け取るのは、システムの写真ピッカーであなたが選んだレシートの写真だけです。写真はアプリ内に保存され、どこにも送信されません。"]),
  ("通知", ["リマインダーとサマリーはローカル通知です。プッシュ通知サーバーを使わず、デバイス上で作成・表示されます。"]),
  ("Aera Proの購入", ["Aera Proのサブスクリプションと購入は、App Storeを通じてAppleが処理します。アプリが知るのはAera Proが有効かどうかだけで、支払い情報を見ることはありません。支払いにはAppleのプライバシーポリシーが適用されます。"]),
  ("バックアップと書き出し", ["バックアップやCSVのファイルは、あなたが指示したときにだけ作成され、「ファイル」やiCloud Driveなど、あなたが選んだ場所に保存されます。その後は保存先サービスの規約が適用されます。iOSでデバイスのiCloudバックアップがオンになっている場合、アプリのデータがAppleの規約に従ってバックアップに含まれることがあります。"]),
  ("データの削除", ["個々の記録はアプリ内で削除できます。デバイスからAeraを削除すると、そのデータもすべて削除されます。"]),
  ("お子さまについて", ["私たちは、お子さまを含め、誰からもデータを収集しません。"]),
  ("本ポリシーの変更", ["本ポリシーを変更する場合は、このページと上部の日付を更新します。"]),
  ("お問い合わせ", ["プライバシーに関するご質問は{contact}までお送りください。よくある質問への回答は{support}ページにあります。"]),
 ],
},
}

# Подписи ссылок между страницами: (политика, поддержка)
LINKS = {
    "ru": ("Политика конфиденциальности", "Поддержка"),
    "en": ("Privacy Policy", "Support"),
    "es": ("Política de privacidad", "Soporte"),
    "pt-BR": ("Política de privacidade", "Suporte"),
    "de": ("Datenschutzerklärung", "Support"),
    "fr": ("Politique de confidentialité", "Assistance"),
    "it": ("Informativa sulla privacy", "Assistenza"),
    "ja": ("プライバシーポリシー", "サポート"),
}

# Страница поддержки (support URL для App Store). Пути по приложению обязаны
# совпадать с реальными экранами — меняешь Настройки, правь и здесь.
SUPPORT = {
"ru": {
 "title": "Поддержка Aera",
 "lead": "Есть вопрос, нашли ошибку или хотите что-то предложить — напишите на {contact}. Ниже ответы на частые вопросы.",
 "sections": [
  ("Как восстановить покупку Aera Pro?", ["Откройте в Aera Настройки и нажмите «Восстановить покупки» под карточкой Aera Pro. Войдите в App Store с тем же Apple ID, с которого оформляли покупку."]),
  ("Как отменить подписку?", ["Подписками управляет Apple: откройте Настройки iPhone → ваше имя → Подписки → Aera. Отменить можно в любой момент, Aera Pro останется доступна до конца оплаченного периода."]),
  ("Как перенести данные на новый iPhone?", ["В Aera откройте Настройки → Данные и резервные копии → «Экспорт резервной копии» и сохраните файл в «Файлы» или iCloud Drive. На новом iPhone выберите там же «Восстановить из копии». Данные Aera переносятся и вместе с резервной копией всего iPhone."]),
  ("Виджет не обновляется или пишет «Aera Pro»", ["Виджеты входят в Aera Pro. Откройте Aera, чтобы виджеты получили свежие данные. Если виджет по-прежнему показывает старое, удалите его с экрана «Домой» и добавьте заново."]),
  ("Конфиденциальность", ["Aera не собирает данные: всё хранится только на вашем устройстве. Подробнее — в документе {privacy}."]),
 ],
},
"en": {
 "title": "Aera Support",
 "lead": "Have a question, found a bug or want to suggest something? Write to {contact}. Answers to common questions are below.",
 "sections": [
  ("How do I restore my Aera Pro purchase?", ["Open Settings in Aera and tap “Restore Purchases” below the Aera Pro card. Make sure you’re signed in to the App Store with the Apple ID you used for the purchase."]),
  ("How do I cancel my subscription?", ["Subscriptions are managed by Apple: open iPhone Settings → your name → Subscriptions → Aera. You can cancel at any time; Aera Pro stays available until the end of the paid period."]),
  ("How do I move my data to a new iPhone?", ["In Aera, open Settings → Data & Backups → “Export Backup” and save the file to Files or iCloud Drive. On the new iPhone, choose “Restore from Backup” in the same place. Aera data is also moved along with a full iPhone backup."]),
  ("A widget doesn’t update or shows “Aera Pro”", ["Widgets are part of Aera Pro. Open Aera so the widgets get fresh data. If a widget still shows old information, remove it from the Home Screen and add it again."]),
  ("Privacy", ["Aera doesn’t collect data: everything stays on your device. See the {privacy} for details."]),
 ],
},
"es": {
 "title": "Soporte de Aera",
 "lead": "¿Tienes una pregunta, has encontrado un error o quieres proponer algo? Escribe a {contact}. Abajo tienes las respuestas a las dudas frecuentes.",
 "sections": [
  ("¿Cómo restauro mi compra de Aera Pro?", ["Abre Ajustes en Aera y toca «Restaurar compras» debajo de la tarjeta de Aera Pro. Inicia sesión en el App Store con el mismo Apple ID con el que hiciste la compra."]),
  ("¿Cómo cancelo la suscripción?", ["Las suscripciones las gestiona Apple: abre Ajustes del iPhone → tu nombre → Suscripciones → Aera. Puedes cancelarla cuando quieras; Aera Pro seguirá disponible hasta el final del periodo pagado."]),
  ("¿Cómo paso mis datos a un iPhone nuevo?", ["En Aera, abre Ajustes → Datos y copias → «Exportar copia de seguridad» y guarda el archivo en Archivos o iCloud Drive. En el iPhone nuevo, elige «Restaurar copia de seguridad» en el mismo lugar. Los datos de Aera también se transfieren con la copia de seguridad completa del iPhone."]),
  ("Un widget no se actualiza o muestra «Aera Pro»", ["Los widgets forman parte de Aera Pro. Abre Aera para que los widgets reciban datos nuevos. Si un widget sigue mostrando información antigua, quítalo de la pantalla de inicio y vuelve a añadirlo."]),
  ("Privacidad", ["Aera no recopila datos: todo se guarda solo en tu dispositivo. Más detalles en la {privacy}."]),
 ],
},
"pt-BR": {
 "title": "Suporte do Aera",
 "lead": "Tem uma dúvida, encontrou um erro ou quer sugerir algo? Escreva para {contact}. Abaixo estão as respostas às perguntas frequentes.",
 "sections": [
  ("Como restaurar minha compra do Aera Pro?", ["Abra os Ajustes no Aera e toque em “Restaurar compras” abaixo do cartão do Aera Pro. Entre na App Store com o mesmo Apple ID usado na compra."]),
  ("Como cancelar a assinatura?", ["As assinaturas são gerenciadas pela Apple: abra Ajustes do iPhone → seu nome → Assinaturas → Aera. Você pode cancelar a qualquer momento; o Aera Pro continua disponível até o fim do período pago."]),
  ("Como passar meus dados para um novo iPhone?", ["No Aera, abra Ajustes → Dados e backups → “Exportar backup” e salve o arquivo no Arquivos ou no iCloud Drive. No novo iPhone, escolha “Restaurar backup” no mesmo lugar. Os dados do Aera também são transferidos com o backup completo do iPhone."]),
  ("O widget não atualiza ou mostra “Aera Pro”", ["Os widgets fazem parte do Aera Pro. Abra o Aera para que os widgets recebam dados atualizados. Se o widget continuar mostrando informações antigas, remova-o da Tela de Início e adicione de novo."]),
  ("Privacidade", ["O Aera não coleta dados: tudo fica só no seu aparelho. Mais detalhes na {privacy}."]),
 ],
},
"de": {
 "title": "Aera Support",
 "lead": "Du hast eine Frage, einen Fehler gefunden oder einen Vorschlag? Schreib an {contact}. Antworten auf häufige Fragen findest du unten.",
 "sections": [
  ("Wie stelle ich meinen Kauf von Aera Pro wieder her?", ["Öffne in Aera die Einstellungen und tippe unter der Aera Pro-Karte auf „Käufe wiederherstellen“. Melde dich im App Store mit der Apple-ID an, mit der du gekauft hast."]),
  ("Wie kündige ich mein Abo?", ["Abos verwaltet Apple: Öffne die iPhone-Einstellungen → dein Name → Abonnements → Aera. Du kannst jederzeit kündigen; Aera Pro bleibt bis zum Ende des bezahlten Zeitraums verfügbar."]),
  ("Wie übertrage ich meine Daten auf ein neues iPhone?", ["Öffne in Aera Einstellungen → Daten & Backups → „Backup exportieren“ und sichere die Datei in „Dateien“ oder iCloud Drive. Wähle auf dem neuen iPhone an derselben Stelle „Aus Backup wiederherstellen“. Die Daten von Aera werden auch mit einem vollständigen iPhone-Backup übertragen."]),
  ("Ein Widget aktualisiert sich nicht oder zeigt „Aera Pro“", ["Widgets sind Teil von Aera Pro. Öffne Aera, damit die Widgets neue Daten erhalten. Zeigt ein Widget weiterhin alte Informationen, entferne es vom Home-Bildschirm und füge es erneut hinzu."]),
  ("Datenschutz", ["Aera erhebt keine Daten: Alles bleibt auf deinem Gerät. Mehr dazu in der {privacy}."]),
 ],
},
"fr": {
 "title": "Assistance Aera",
 "lead": "Une question, un bug ou une suggestion ? Écrivez à {contact}. Vous trouverez ci-dessous les réponses aux questions fréquentes.",
 "sections": [
  ("Comment restaurer mon achat Aera Pro ?", ["Ouvrez les Réglages d’Aera et touchez « Restaurer les achats » sous la carte Aera Pro. Connectez-vous à l’App Store avec l’identifiant Apple utilisé pour l’achat."]),
  ("Comment résilier mon abonnement ?", ["Les abonnements sont gérés par Apple : ouvrez Réglages de l’iPhone → votre nom → Abonnements → Aera. Vous pouvez résilier à tout moment ; Aera Pro reste disponible jusqu’à la fin de la période payée."]),
  ("Comment transférer mes données vers un nouvel iPhone ?", ["Dans Aera, ouvrez Réglages → Données et sauvegardes → « Exporter une sauvegarde » et enregistrez le fichier dans Fichiers ou iCloud Drive. Sur le nouvel iPhone, choisissez « Restaurer une sauvegarde » au même endroit. Les données d’Aera sont aussi transférées avec une sauvegarde complète de l’iPhone."]),
  ("Un widget ne se met pas à jour ou affiche « Aera Pro »", ["Les widgets font partie d’Aera Pro. Ouvrez Aera pour que les widgets reçoivent des données à jour. Si un widget affiche encore d’anciennes informations, retirez-le de l’écran d’accueil et ajoutez-le de nouveau."]),
  ("Confidentialité", ["Aera ne collecte aucune donnée : tout reste sur votre appareil. Plus de détails dans la {privacy}."]),
 ],
},
"it": {
 "title": "Assistenza Aera",
 "lead": "Hai una domanda, hai trovato un errore o vuoi proporre qualcosa? Scrivi a {contact}. Qui sotto trovi le risposte alle domande frequenti.",
 "sections": [
  ("Come ripristino l’acquisto di Aera Pro?", ["Apri le Impostazioni di Aera e tocca «Ripristina acquisti» sotto la scheda Aera Pro. Accedi all’App Store con lo stesso ID Apple usato per l’acquisto."]),
  ("Come disdico l’abbonamento?", ["Gli abbonamenti sono gestiti da Apple: apri Impostazioni dell’iPhone → il tuo nome → Abbonamenti → Aera. Puoi disdire in qualsiasi momento; Aera Pro resta disponibile fino alla fine del periodo pagato."]),
  ("Come trasferisco i dati su un nuovo iPhone?", ["In Aera apri Impostazioni → Dati e backup → «Esporta backup» e salva il file in File o iCloud Drive. Sul nuovo iPhone scegli «Ripristina da backup» nello stesso punto. I dati di Aera vengono trasferiti anche con il backup completo dell’iPhone."]),
  ("Un widget non si aggiorna o mostra «Aera Pro»", ["I widget fanno parte di Aera Pro. Apri Aera perché i widget ricevano dati aggiornati. Se un widget mostra ancora informazioni vecchie, rimuovilo dalla schermata Home e aggiungilo di nuovo."]),
  ("Privacy", ["Aera non raccoglie dati: tutto resta sul tuo dispositivo. Maggiori dettagli nell’{privacy}."]),
 ],
},
"ja": {
 "title": "Aera サポート",
 "lead": "ご質問、不具合のご報告、ご提案は{contact}までお送りください。よくある質問への回答は以下のとおりです。",
 "sections": [
  ("Aera Proの購入を復元するには？", ["Aeraの設定を開き、Aera Proカードの下にある「購入を復元」をタップします。購入時と同じApple IDでApp Storeにサインインしてください。"]),
  ("サブスクリプションを解約するには？", ["サブスクリプションはAppleが管理しています。iPhoneの設定 → ユーザ名 → サブスクリプション → Aeraを開いてください。いつでも解約でき、支払い済みの期間が終わるまでAera Proを利用できます。"]),
  ("新しいiPhoneにデータを移すには？", ["Aeraで設定 → データとバックアップ → 「バックアップを書き出す」を開き、ファイルを「ファイル」またはiCloud Driveに保存します。新しいiPhoneでは同じ場所で「バックアップから復元」を選びます。iPhone全体のバックアップでもAeraのデータは移行されます。"]),
  ("ウィジェットが更新されない・「Aera Pro」と表示される", ["ウィジェットはAera Proの機能です。Aeraを開くと、ウィジェットに最新のデータが反映されます。古い情報のままの場合は、ホーム画面からウィジェットを削除して、もう一度追加してください。"]),
  ("プライバシー", ["Aeraはデータを収集しません。すべてのデータはお使いのデバイスにのみ保存されます。詳しくは{privacy}をご覧ください。"]),
 ],
},
}

UI = {  # подпись переключателя языка для скринридеров
    "ru": "Язык", "en": "Language", "es": "Idioma", "pt-BR": "Idioma",
    "de": "Sprache", "fr": "Langue", "it": "Lingua", "ja": "言語",
}


def contact_html(lang: str) -> str:
    return f'<a href="{escape(CONTACT_URL)}">{escape(CONTACT_EMAIL)}</a>'


def fill(text: str, lang: str) -> str:
    """Подстановки в текстах: {contact} — почта, {privacy} и {support} — ссылки
    между страницами с тем же языком."""
    html = escape(text).replace("{contact}", contact_html(lang))
    html = html.replace("{privacy}", f'<a href="./?lang={lang}">{escape(LINKS[lang][0])}</a>')
    html = html.replace("{support}", f'<a href="support.html?lang={lang}">{escape(LINKS[lang][1])}</a>')
    return html


def article(lang: str, content: dict) -> str:
    t = content[lang]
    parts = [f'<article lang="{lang}" data-lang="{lang}"{"" if lang == "en" else " hidden"}>',
             f'<h1>{escape(t["title"])}</h1>']
    if "updated" in t:
        parts.append(f'<p class="updated"><time datetime="{UPDATED_ISO}">{escape(t["updated"])}</time></p>')
    parts.append(f'<p class="lead">{fill(t["lead"], lang)}</p>')
    for heading, paragraphs in t["sections"]:
        parts.append(f"<section><h2>{escape(heading)}</h2>")
        for p in paragraphs:
            parts.append("<p>" + fill(p, lang) + "</p>")
        parts.append("</section>")
    parts.append("</article>")
    return "\n".join(parts)


def page(content: dict, title: str, description: str) -> str:
    assert set(content) == {code for code, _ in LANGS}
    sizes = {len(content[l]["sections"]) for l in content}
    assert len(sizes) == 1, "во всех языках должно быть одинаковое число разделов"
    buttons = "\n".join(
        f'<button type="button" data-set-lang="{code}" lang="{code}">{escape(name)}</button>'
        for code, name in LANGS)
    articles = "\n".join(article(code, content) for code, _ in LANGS)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)}</title>
<meta name="description" content="{escape(description)}">
<style>
:root {{
  --bg: #ffffff; --ink: #1d1d1f; --muted: #6e6e73; --line: #d2d2d7;
  --accent: #0071e3; --chip: #f5f5f7; --chip-on: #1d1d1f; --chip-on-ink: #ffffff;
}}
@media (prefers-color-scheme: dark) {{
  :root {{
    --bg: #000000; --ink: #f5f5f7; --muted: #a1a1a6; --line: #424245;
    --accent: #2997ff; --chip: #1d1d1f; --chip-on: #f5f5f7; --chip-on-ink: #000000;
  }}
}}
* {{ box-sizing: border-box; }}
html {{ -webkit-text-size-adjust: 100%; }}
body {{
  margin: 0; background: var(--bg); color: var(--ink);
  font: 17px/1.55 -apple-system, BlinkMacSystemFont, "SF Pro Text", "Helvetica Neue",
        "Hiragino Sans", "Noto Sans JP", Arial, sans-serif;
}}
main {{ max-width: 680px; margin: 0 auto; padding: 28px 16px 72px; }}
nav {{ display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 40px; }}
nav button {{
  font: inherit; font-size: 14px; border: 0; border-radius: 980px;
  padding: 6px 14px; background: var(--chip); color: var(--ink); cursor: pointer;
}}
nav button[aria-pressed="true"] {{ background: var(--chip-on); color: var(--chip-on-ink); }}
nav button:focus-visible {{ outline: 2px solid var(--accent); outline-offset: 2px; }}
h1 {{ font-size: clamp(28px, 6vw, 44px); line-height: 1.1; letter-spacing: -0.02em; margin: 0 0 12px;
      hyphens: auto; -webkit-hyphens: auto; overflow-wrap: break-word; }}
.updated {{ color: var(--muted); font-size: 15px; margin: 0 0 28px; }}
.lead {{ font-size: 21px; line-height: 1.45; margin: 0 0 40px; }}
section {{ border-top: 1px solid var(--line); padding-top: 22px; margin-top: 22px; }}
h2 {{ font-size: 21px; letter-spacing: -0.01em; margin: 0 0 8px; }}
p {{ margin: 0 0 12px; }}
a {{ color: var(--accent); text-decoration: none; }}
a:hover {{ text-decoration: underline; }}
</style>
</head>
<body>
<main>
<nav aria-label="Language">
{buttons}
</nav>
{articles}
</main>
<script>
(function () {{
  var codes = {[c for c, _ in LANGS]!r};
  var labels = {UI!r};
  function pick(raw) {{
    if (!raw) return null;
    raw = raw.toLowerCase();
    for (var i = 0; i < codes.length; i++) {{
      var c = codes[i].toLowerCase();
      if (raw === c || raw.split("-")[0] === c.split("-")[0]) return codes[i];
    }}
    return null;
  }}
  function show(code) {{
    document.querySelectorAll("article").forEach(function (a) {{
      a.hidden = a.getAttribute("data-lang") !== code;
    }});
    document.querySelectorAll("nav button").forEach(function (b) {{
      b.setAttribute("aria-pressed", String(b.getAttribute("data-set-lang") === code));
    }});
    document.documentElement.lang = code;
    document.querySelector("nav").setAttribute("aria-label", labels[code] || "Language");
    var h = document.querySelector('article[data-lang="' + code + '"] h1');
    if (h) document.title = h.textContent;
  }}
  var q = new URLSearchParams(location.search).get("lang");
  var langs = navigator.languages || [navigator.language];
  var start = pick(q);
  for (var i = 0; !start && i < langs.length; i++) start = pick(langs[i]);
  show(start || "en");
  document.querySelectorAll("nav button").forEach(function (b) {{
    b.addEventListener("click", function () {{
      var code = b.getAttribute("data-set-lang");
      show(code);
      var url = new URL(location.href);
      url.searchParams.set("lang", code);
      history.replaceState(null, "", url);
    }});
  }});
}})();
</script>
</body>
</html>
"""


if __name__ == "__main__":
    here = Path(__file__).parent
    pages = [
        ("index.html", T, "Aera — Privacy Policy", "Aera does not collect your data. Everything stays on your device."),
        ("support.html", SUPPORT, "Aera — Support", "Help with Aera: purchases, subscriptions, moving data and widgets."),
    ]
    for name, content, title, description in pages:
        (here / name).write_text(page(content, title, description), encoding="utf-8")
        print("written", here / name)
