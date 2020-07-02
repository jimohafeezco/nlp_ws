#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.

"""
First, a few callback functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Example of a bot-user conversation using ConversationHandler.
Send /start to initiate the conversation.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging
token= 
from telegram import ReplyKeyboardMarkup
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler)
logger = logging.getLogger(__name__)

COUNTRY, CITY, REGION, STATE, RESTART = range(5)

main_menu =[["/start"]]
reply_keyboard_country=[["Nigeria","Ghana", "Togo", "Done"]]
reply_keyboard_state = [["Osun", "Lagos", "Kaduna", "Done"]]
reply_keyboard_city =[["Berlin","Moscow","London", "Done"]]
reply_keyboard_region =[["SW","SE", "NE", "Done"]]

markup_main= ReplyKeyboardMarkup(main_menu, resize_keyboard=True, one_time_keyboard=True)
markup_country = ReplyKeyboardMarkup(reply_keyboard_country, resize_keyboard=True, one_time_keyboard=True)
markup_region = ReplyKeyboardMarkup(reply_keyboard_region, resize_keyboard=True,one_time_keyboard=True)
markup_city = ReplyKeyboardMarkup(reply_keyboard_city,resize_keyboard=True, one_time_keyboard=True)
markup_state = ReplyKeyboardMarkup(reply_keyboard_state, resize_keyboard=True,one_time_keyboard=True)

def start(update, context):
    text = update.message.text
    context.user_data['choice'] = text
    if update.message.text =='Done':
        # choose_city(update,context)
        cancel(update, context)
        return ConversationHandler.END
    update.message.reply_text(
        "Why don't you tell me were you are from",
        reply_markup=markup_country)
    return COUNTRY


def choose_country(update, context):
    text = update.message.text
    context.user_data['choice'] = text
    if update.message.text =='Done':
        cancel(update, context)
        return ConversationHandler.END
    update.message.reply_text(
        'Yes, I would love to know which region you are from!',

        reply_markup = markup_region)
    return REGION


def choose_region(update, context):
    text = update.message.text
    context.user_data['choice'] = text
    if update.message.text =='Done':
        cancel(update, context)
        return ConversationHandler.END
    update.message.reply_text(
        'Yes, I would love to know which state you are from!', 
        reply_markup= markup_state)
    return STATE

def choose_state(update, context):
    text = update.message.text
    context.user_data['choice'] = text
    if update.message.text =='Done':
        cancel(update, context)
        return ConversationHandler.END
    update.message.reply_text(
        'Yes, I would love to know which city you are from!', 
        reply_markup= markup_city)
    return CITY

def choose_city(update, context):
    text = update.message.text
    context.user_data['choice'] = text
    if update.message.text =='Done':
        cancel(update, context)
        return ConversationHandler.END
    update.message.reply_text(
        'Thank you for providing this information',markup_city)
    return ConversationHandler.END


def cancel(update, context):
    update.message.reply_text("Cancelling...\n Why don't you tell me were you are from",
     reply_markup=markup_country)
    # start(update, context)
    return  COUNTRY

def main():
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(token, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add conversation handler with the states CHOOSING, TYPING_CHOICE and TYPING_REPLY

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],

        states={
            COUNTRY: [MessageHandler(Filters.text,
                                      choose_country),
                                      ],
            REGION: [MessageHandler(Filters.text,
                                      choose_region),
                                      ],                         
            STATE: [MessageHandler(Filters.text,
                                      choose_state),
                                      ],                       
            CITY: [MessageHandler(Filters.text,
                                      choose_city),
                                      ],     
            RESTART: [MessageHandler(Filters.text,
                                      choose_country),
                                      ], 
        },allow_reentry=1,

        fallbacks=[MessageHandler(Filters.regex('^Done$'), cancel)]
    )
    # start_handler =CommandHandler("start", start)
    # dp.add_handler(start_handler)
    dp.add_handler(conv_handler)

    # log all errors
    # dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
