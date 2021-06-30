from botbuilder.core import (
    CardFactory,
    TurnContext
)
from botbuilder.schema import HeroCard, CardImage
from botbuilder.schema.teams import (
    MessagingExtensionAction,
    MessagingExtensionActionResponse,
    MessagingExtensionAttachment,
    MessagingExtensionResult,
)
from botbuilder.core.teams import TeamsActivityHandler
import json
from datetime import datetime as dt, timedelta as td
from locale import setlocale, LC_ALL

class TeamsMessagingExtensionsActionBot(TeamsActivityHandler):
    async def on_teams_messaging_extension_submit_action_dispatch(
        self, turn_context: TurnContext, action: MessagingExtensionAction
    ) -> MessagingExtensionActionResponse:
        if action.command_id == "QuickQuote":
            return await self.quote_message(turn_context, action)

        raise NotImplementedError(f"Unexpected action.command_id {action.command_id}.")

    async def quote_message(
        self,
        turn_context: TurnContext,  # pylint: disable=unused-argument
        action: MessagingExtensionAction,
    ) -> MessagingExtensionActionResponse:
        # Обработка нажатия команды "Цитировать"
        # Установливаем локаль
        setlocale(LC_ALL, "")
        # Определяем дату цитируемого сообщения
        date_created = dt.strptime(action.message_payload.created_date_time, "%Y-%m-%dT%H:%M:%S.%fZ")
        date_created = date_created + td(hours=5) # почему-то дата приходит меньше на 5 часов от того, что показано в Тимс
        date_created = date_created.astimezone()
        if date_created.date() == dt.now().date():
            str_date = date_created.strftime("%H:%M")
        else:
            str_date = date_created.strftime("%d.%m.%Y %H:%M")
        # Определяем автора цитируемого сообщения
        display_name = f"{action.message_payload.from_property.user.display_name}:"
        # Определяем контент
        text = action.message_payload.body.content

        # Формируем карточку ответа
        card = HeroCard(text="<blockquote><em><small>" + 
                        str_date + "</small>\n\n" + "<strong>" + 
                        display_name + "</strong>\n\n<p>" + 
                        text + "</p></em></blockquote>\n\n")
        content_type = CardFactory.content_types.hero_card
        # На основании карточки ответа формируем вложение
        attachment = MessagingExtensionAttachment(
            content=card,
            content_type=content_type,
            preview=CardFactory.hero_card(card)
        )    
        # Формируем ответ
        extension_result = MessagingExtensionResult(
            attachment_layout="list", type="result", attachments=[attachment]
        )

        return MessagingExtensionActionResponse(compose_extension=extension_result)

