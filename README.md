# ZUIL-BackEnd
Zuil Uitleen voor Informatica Leermaterialen

# Code Contract

## Gemaakt door Tim Banh voor de Back-End van het project ZUIL

 Hierin hebben wij onze afspraken staan over hoe wij te werk gaan met onze code. Wij zijn hier in overleg tot gekomen en staan hier allebei achter. We hebben samen alle onderstaande onderwerpen besproken en zijn samen tot het volgende contract gekomen.

---

## Inhoud

1. Afspraken naamgevingen
2. Styles van naamgevingen
3. GIT en project structuur
4. Taal
5. Inspringen
6. Wit regels
7. Maximum regel lengte

---

### Afspraken naamgevingen

> Voor de Naamgevingen hebben we de afgesproken om gebruik te maken van kleine letters en bij opgesplitste woorden wordt er een laag streepje gebruikt voor variabelen en functies. We zullen voor classes gebruik gaan maken van PascalCasing. We hebben voor deze optie gekozen om gemakkelijk onderscheidd te kunnen maken tussen variabelen/functies en classes.

---

### Styles van naamgevingen

> Voor de style van naamgevingen gaan wij gebruik maken van een aantal regels:

> - We gaan geen gebruik maken van afkortingen om zo de leesbaarheid te verhogen en verwarring te voorkomen. **Voorbeeld: employeeId ipv eId**
> - We zullen variabelen gehele namen geven om zo duidelijk onderscheid te houden. **Voorbeeld: employee_name ipv Name**
> - We zullen in loops wel gebruik maken van eenletterige variabelen zodat deze niet in zoekvelden naar voren komen en verwarring veroorzaken. We gebruiken alleen niet de letter O & I hiervoor, omdat dit kan gelezen worden als 1 of 0.
> - Voor functies zullen we gebruik maken van werkwoorden in de naamgevingen zodat er een duidelijk is tussen klasses en functies.
> - Code schoon houden en geen gebruik maken van onzin naamgevingen die grappig bedoeld zijn. **Voorbeeld: GetBalance() ipv ShowMeTheMoney()**

---

### GIT en project structuur

> Voor GIT hebben wij een aantal regels opgesteld waar wij ons beiden aan zullen moeten houden om een duidelijke structuur te behouden:
>
> - We zullen gebruik maken van GitHub Desktop of Git Kraken.
> - We zullen gebruik maken van versiebeheer. Hierbij word de versie verhoogt met 1.0 tot gehele getallen. **Voorbeeld: 1.0 -> 2.0 ... -> 1.1.0**
> - We zullen bij onze branches naamgevingen hanteren als volgt: onderwerp + functionaliteit. **Voorbeeld: API-uitlezen**
> - We zullen bij onze commits naamgevingen hanteren als volgt: featurenaam + versienummer. **Voorbeeld: API-uitlezen1.0 -> API-uitlezen1.1**
> - We zullen bij onze commits ook commentaar leveren over welke veranderingen zijn doorgevoerd.

---

### Taal

> Onze applicatie zullen we volledig in het engels gaan ontwikkelen. Hierbij zullen we zowel code als commentaar in het engels schrijven.

---

### Inspringen

> Het inspringingsniveau van regels code in Python bepaalt hoe statements bij elkaar worden gegroepeerd. Het is dus belangrijk om in te springen op de volgende regel na bv een if statement. Voor het inspringen gebruiken we tabs.

**VB:**
```python
if x == y
    print(x)
```

---

### Wit regels

> Voor het project hebben wij afgesproken om 1 witregel tussen functies in te zetten.
> Binnen een functie zullen witregels gebruikt worden op de manier dat de code overzichtelijk blijft. Bijvoorbeeld denk aan het scheiden van variabelen of statements.

---

### Maximum regel lengte

> In het project zullen wij de maximum regel lengte houden op 79 tekens.
