# Importing required libraries
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Penalty, Driver
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.middleware import csrf
import json

def index(request):
    """Function for index view."""

    # Returning response
    response = render(request, "index.html")
    return responseHeadersModifier(response)

def register(request):
    """Function for registration view."""

    # If GET request
    if request.method == "GET":

        # Returning response
        response = render(request, "register.html")
        return responseHeadersModifier(response)

    # If POST request
    elif request.method == "POST":

        # Extracting data from POST request
        name = request.POST["userName"]
        email = request.POST["userEmail"]
        password = request.POST["userPassword"]
        confirmPassword = request.POST["userConfirmPassword"]
        RFID = request.POST["userRFID"]

        # Checking if passwords don't match
        if password != confirmPassword:

            # Failure message if passwords don't match
            context = {
                "Failure": "Passwords don't match."
            }

            # Returning response
            response = render(request, "register.html", context)
            return responseHeadersModifier(response)

        # Creating user
        user = User.objects.create_user(name, email, password)

        # Creating driver and associating to user
        driver = Driver(user = user, RFID = RFID)
        driver.save()

        # Returning response
        response = render(request, "login.html")
        return responseHeadersModifier(response)

def loginUser(request):
    """Function for login view."""

    # If GET request
    if request.method == "GET":

        # Returning response with login html page
        response = render(request, "login.html")
        return responseHeadersModifier(response)

    # If POST request
    elif request.method == "POST":

        # Extracting data from POST request
        username = request.POST["userName"]
        password = request.POST["userPassword"]

        # Authenticating username password
        user = authenticate(request, username = username, password = password)

        # If user authenticated successfully and user returned
        if user is not None:

            # Logging in (session)
            login(request, user)

            # Returning response with index html page
            response = render(request, "index.html")
            return responseHeadersModifier(response)

        # If no user found, user credentials wrong
        else:

            # Failure message
            context = {
                "Failure": "Invalid credentials."
            }

            # Returning response
            response = render(request, "login.html", context)
            return responseHeadersModifier(response)

def logoutUser(request):
    """Function for logout view."""

    # If user is logged in
    if request.user.is_authenticated:

        # Logging out
        logout(request)

        # Returning response
        response = render(request, "login.html")
        return responseHeadersModifier(response)

    # If user not logged in
    else:

        # Returning response
        response = render(request, "login.html")
        return responseHeadersModifier(response)


def getPenalties(request, RFID):
    """API for getting penalties of a user RFID through RaspiRFIDSystem."""

    # If user is logged in
    if request.user.is_authenticated:

        # Returning JSON response with the penalties of user RFID
        return JsonResponse({
            "Penalties": list(Penalty.objects.filter(RFID = RFID).values())
        })
    # If user is not logged in
    else:

        # Returning failure response
        return JsonResponse({
            "Failure": "Please login first."
        })

def submitPenalty(request):
    """API for submitting penalty through RaspiRFIDSystem."""

    # If POST request
    if request.method == "POST":

        # If user is logged in
        if request.user.is_authenticated:

            # Getting data from POST request
            RFID = request.POST["RFID"]
            status = request.POST["status"]
            amount = int(request.POST["amount"])
            type = request.POST["type"]

            # Creating and saving new penalty
            penalty = Penalty(RFID = RFID, status = status, amount = amount, type = type)
            penalty.save()

            # Returning response
            return JsonResponse({
                "Success": f"Successfully submitted.\n{str(penalty)}"
            })
        # If user is not logged in
        else:

            # Returning JSON response with failure message
            return JsonResponse({
                "Failure": "Please login first."
            })
    # If GET request
    else:

        # Returning new csrf token
        return JsonResponse({
            "csrfmiddlewaretoken": csrf.get_token(request)
        })

def payPenalty(request):
    """API to pay penalty (change penalty payment status) through RaspiRFIDSystem."""

    # If POST request
    if request.method == "POST":

        # If user is logged in
        if request.user.is_authenticated:

            # Extracting data from POST request
            penaltyID = int(request.POST["penaltyID"])

            # Getting penalty, changing status to paid, then saving
            penalty = Penalty.objects.get(pk = penaltyID)
            penalty.status = "Paid"
            penalty.save()

            # Returning response
            return JsonResponse({
                "Success": f"Successfully updated.\n{str(penalty)}"
            })
        # If user is not logged in
        else:

            # Returning JSON response with failure message
            return JsonResponse({
                "Failure": "Please login first."
            })
    # If GET request
    else:

        # Returning new csrf token
        return JsonResponse({
            "csrfmiddlewaretoken": csrf.get_token(request)
        })

def summary(request):
    """Function for summary view. Shows all penalties of user RFID."""

    # If user is logged in
    if request.user.is_authenticated:

        # Getting user RFID penalties
        context = {
            "penalties": Penalty.objects.filter(RFID = request.user.driver.RFID)
        }

        # Returning response
        response = render(request, "summary.html", context)
        return responseHeadersModifier(response)

    # If the user is not logged in
    else:

        # Returning response with index page
        response = render(request, "index.html")
        return responseHeadersModifier(response)

def contactus(request):
    """Function for contact us view."""

    # Returning response
    response = render(request, "contactus.html")
    return responseHeadersModifier(response)


def responseHeadersModifier(response):
    """Funtion to edit response headers so that no cached versions can be viewed. Returns the modified response."""

    # Modifying response headers
    response["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response["Pragma"] = "no-cache"
    response["Expires"] = "0"

    # Returning response
    return response
