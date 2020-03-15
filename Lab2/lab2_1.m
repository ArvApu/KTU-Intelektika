clc, clear, close all;
load sunspot.txt;

plot_sunspots(sunspot)

n = 2; % autoregresinio modelio eile

L = length(sunspot); % duomenu kiekis
P = [sunspot(1:L-2,2)'; sunspot(2:L-1, 2)']; % ivesties duomenu matrica
T = sunspot(3:L, 2)'; % isvesties duomenu vektorius

plot_sunspots_3d(P, T)

Pu = P(:, 1:200); % apmokymo duomenu matrica
Tu = T(:, 1:200); % apmokymo rezultatu matrica

[net,w1,w2,b] = create_neuron(Pu, Tu);

Tsu = sim(net, Pu); % neurono veikimo simuliacija
plot_forecast_1(Tu, Tsu, sunspot);

Ts = sim(net, P); % neurono veikimo simuliacija
plot_forecast_2(T, Ts, sunspot);

e = T - Ts; % prognozes klaidos vekotrius
plot_forecast_error(e, sunspot);

hist_forecast_error(e);
mse_value = mse(e); % average squared forecast error value
mad_value = mad(e); % median absolute deviation

function plot_sunspots(sunspot)
    figure(1);
    plot(sunspot(:,1),sunspot(:,2),'g-*');

    grid on;
    
    xlabel('Year')
    ylabel('Sun activity days')
    
    title('Days of sun activity on every year')
end

function plot_sunspots_3d(P, T)
    figure(2);
    plot3(P(1,:), P(2,:), T, 'mo');
    
    grid on;
    
    xlabel('Sun spots count on (n-2) year');
    ylabel('Sun spots count on (n-1) year');
    zlabel('Sun spots count on (n-0) year');
    
    title('Sun spots forecast, based on last 2 years');
end

function [net,w1,w2,b] = create_neuron(Pu, Tu)
    net = newlind(Pu, Tu);
    
    disp('Neuron weight coefficients:');
    disp(net.IW{1});
    
    disp('Neuron bias value:');
    disp(net.b{1});

    w1 = net.IW{1}(1);
    w2 = net.IW{1}(2);
    b  = net.b{1};
end

function plot_forecast_1(Tu, Tsu, sunspot)
    figure(3), hold on;
    
    plot(sunspot(3:202, 1), Tu, 'r-o');
    plot(sunspot(3:202, 1), Tsu, 'b-o');
    
    xlabel('Year');
    ylabel('Sun activity days')
    
    grid on;
    
    legend('Real spots values', 'Forecast of spots values');
    title('Sunspots forecast quality verification for years of 1702-1901');
end

function plot_forecast_2(T, Ts, sunspot)
    figure(4), hold on;
    
    plot(sunspot(3:315, 1), T, 'r-o');
    plot(sunspot(3:315, 1), Ts, 'b-o');
    
    xlabel('Year');
    ylabel('Sun activity days')
    
    grid on;
    
    legend('Real spots values', 'Forecast of spots values');
    title('Sunspots forecast quality verification for years of 1702-2014');
end

function plot_forecast_error(e, sunspot)
    figure(5);
    plot(sunspot(3:315), e, 'r-x');
    
    grid on;

    xlabel('Year');
    ylabel('Spots count difference between real and forecast values');
    
    title('Forecast errors diagram for years of 1702-2014');
end

function hist_forecast_error(e)
    figure(6);
    hist(e);
    
    xlabel('Forecast error value');
    ylabel('Frequency');
    
    title('Forecast error histogram');
end
