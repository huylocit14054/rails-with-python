class FactorialController < ApplicationController

    #display input form
    def new
        @result = 0 
        puts @result
    end 

    #calculate the 
    def calculate_factorial
        @number = params[:input][:number]
        #@script = "python factorial.py " + @number 
        @result = `python factorial.py #{@number}`
        render 'new'
    end 
end
